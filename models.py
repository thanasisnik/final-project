from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# defining our tables

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False, unique = True)
    hash = db.Column(db.String(200), nullable = False)

class Tables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable = False, unique= True)

    # make the relationship with order
    orders = db.relationship('Orders', uselist = False, primaryjoin="and_(Tables.id == Orders.table_id, Orders.status == False)")

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False) 
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    items = db.relationship('OrderItems', backref='order', lazy=True)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p_name = db.Column(db.String(80), nullable=False, unique=True)
    price = db.Column(db.Numeric(10,2), nullable=False)

class OrderItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    qty = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Numeric(10,2), nullable=False)
    product = db.relationship('Products', backref = 'order-items', lazy = True)

