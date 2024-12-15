from flask import flash, render_template, request, redirect, session, jsonify
from models import db, Users, Tables, Products, OrderItems, Orders
from helpers import apology, login_required
from sqlalchemy import text
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import current_user

def register_routes(app):

    @app.after_request
    def after_request(response):
        """Ensure responses aren't cached"""
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

    #INDEX ROUTE 
    @app.route("/", methods=["POST", "GET"])
    @login_required
    def index():
        #display all tables from the database
        tables = Tables.query.all()
        if request.method == "POST":
            table_number = request.form.get("table_number")
            if not table_number:
                return apology("Missing table number", 400)
            #insert table
            new_table = Tables(table_number = table_number)
            db.session.add(new_table) 
            db.session.commit()
            return jsonify({"table_number":table_number})
        else:
            return render_template("index.html", tables=tables)    
    
    #
    @app.route("/add_table", methods=["POST"])
    @login_required
    def add_table():
        table_number = request.form.get("table_number")
        if not table_number:
            return apology("Missing table number", 400)
        new_table = Tables(table_number = table_number)
        db.session.add(new_table)
        db.session.commit()
        return jsonify({"table_number": table_number})
    

    #Route for adding products to the menu.
    @app.route("/add_product", methods=["POST", "GET"])
    @login_required
    def add_product():
        products = Products.query.all()
        if request.method == "POST":
            p_name = request.form.get("product")
            p_price = request.form.get("price")

            #Check if inputs fields exists
            if not p_name or not p_price:
                return apology("Product name and price are required",400)
            
            #Check if the price of the product is positive
            try:
                price = float(p_price)
                if price < 0: 
                    return apology("Price must be positive",400)
                
                #Insert the new product 
                new_product = Products(p_name=p_name, price = price)
                db.session.add(new_product)
                db.session.commit()
                return jsonify({"id": new_product.id, "p_name": new_product.p_name, "price": str(new_product.price)})
            except Exception as e:
                db.session.rollback()
                return apology (str(e),500)
        else:
            return render_template("products.html", products=products)



    #Creating orders using table id from URL parameter
    @app.route("/order/<int:table_id>", methods=["GET","POST"])
    @login_required
    def order(table_id):
            #show the products already inserted so
            #the user can easily add the product to the order
            products = Products.query.all()
            table = Tables.query.get_or_404(table_id)

            if request.method == "POST":
                #retrieve the data as JSON
                data = request.json;
                if not data:
                    return apology("Invalid data", 400)
                
                #create a new order where the table id is the parameter we get from url
                order = Orders.query.filter_by(table_id=table_id, status=False).first()
                if not order:
                    order = Orders(table_id=table_id, status=False)
                    db.session.add(order)
                    db.session.commit()
                
                #Iterate through each item in the received json data
                #we get the product from Products table using the id
                for item in data:
                    product = Products.query.get(item["id"])
                    #if product with this id dont exists skip to the next item
                    if not product:
                        continue
                    #else we insert at order items the order_id and the product id, price with a defualt
                    #quanity = 1
                    add = OrderItems(
                        order_id = order.id,
                        product_id = product.id,
                        qty = 1, #default
                        price = product.price

                    )
                    db.session.add(add)
                db.session.commit()
                
                return redirect("/")
            else:
                #if we have already an existing order at that table 
                #then we will show that order and we will show the total amount (cost) of the order
                exists = Orders.query.filter_by(table_id=table_id, status=False).first()
                total_amount = 0
                if exists:
                    total_amount = sum(item.price * item.qty for item in exists.items)

                return render_template("/orders.html", products=products, table=table, exists=exists, total_amount=total_amount)


    #Route to close the table's order
    @app.route("/order/<int:table_id>/close" , methods=["POST"])
    @login_required
    def close_table(table_id):
        order = Orders.query.filter_by(table_id = table_id, status=False).first()
        if not order:
            return apology("No active order found", 404)
        # When the order status becomes True
        # the order is paid and we can continue with next orders
        order.status = True
        db.session.commit()

        return redirect("/")


    #Settings route
    @app.route("/settings", methods=["GET","POST"])
    @login_required
    def settings():
        if request.method == "POST":
            crnt_password = request.form.get("crnt_password")
            new = request.form.get("new_password")
            confirm = request.form.get("confirmation")

            user = Users.query.get(session["user_id"])

            #We use the check_password_hash function to check if
            #the current_password inserted from user is the same
            #with the password stored at the users database.
            #if its right and new password == confirmation password
            # we save the new password at the users db.
            if not check_password_hash(user.hash, crnt_password):
                return apology("wrong password", 400 )
            if new != confirm:
                return apology("passwords dont match!", 400)
            
            user.hash = generate_password_hash(new)
            db.session.commit()
            flash("Password updates successfully!")
            return redirect("/")
        else:
            return render_template("/settings.html")
        

    #This route returns the sales statistics of the products
    #explain this further at the documentation how the query work for that.
    @app.route("/statistics")
    @login_required
    def statistics():
        statistics = db.session.query(Products.p_name, db.func.sum(OrderItems.qty).label("qty")).join(OrderItems, Products.id == OrderItems.product_id).group_by(Products.id).order_by(db.func.sum(OrderItems.qty).desc()).all()

        products = [{"name":statistic.p_name, "qty":statistic.qty,} for statistic in statistics]
        return render_template("statistics.html", products=products)

    # A simple Register route
    @app.route("/register", methods = ["POST", "GET"])
    def register():
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            confirmation = request.form.get("confirmation")
            
            # we check if username and password exists in form 
            if not request.form.get("username"):
                return apology("Blank username", 400)

            if not request.form.get("password"):
                return apology("Blank password", 400)

            if not request.form.get("confirmation"):
                return apology("Blank confirmation")

            # we check if password is the same with the confirmation password
            if request.form.get("password") != request.form.get("confirmation"):
                return apology("Passwords dont match", 400)
            
            
            user = Users.query.filter_by(username = request.form.get("username")).first()
            # we check if the username already exists 
            # username is unique for this project app. 
            if user:
                return apology("Username already exists")
            
            hashed_password = generate_password_hash(password)
            # insert the user at the table.
            new_user = Users(username=username, hash=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            
            return redirect("/")
        
        elif request.method == "GET":
            return render_template("register.html")
        
    # A simple Login route 
    @app.route("/login", methods=["POST", "GET"])
    def login():

        session.clear() #forget any user_id

        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")
            if not username:
                return apology("Username required", 400)
            if not password:
                return apology("Password required", 400)
            
            #query database for username
            user = Users.query.filter_by(username = username).first()

            #check if exists and password is correct
            if user is None or not check_password_hash(user.hash, password):
                return apology("Invalid Username and/or Password", 400)
            
            session["user_id"] = user.id
            return redirect ("/")

        else:
            return render_template("login.html")
        

    @app.route("/logout")
    def logout():
        """Log user out"""

        # Forget any user_id
        session.clear()

        # Redirect user to login form
        return redirect("/")
