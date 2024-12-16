# final-project
#### Video Demo:  <URL HERE>
#### Description:
This repository contains a web application designed to help users efficiently manage orders remotely for businesses such as restaurants, coffee shops, and similar establishments. The application provides a simple interface for recording, editing, and closing orders in real time, improving operational efficiency and remote communication.

## Features
1.  Add the tables of your business
    Users can easily add tables just by entering the table number.
2.  Add your products
    Users can add products just by entering the name and the price.
3.  Add new orders
    Send new orders by selecting the table and add the products.
4.  Update existing orders
    If a customer update their order, we update the existing order in real time.
5.  Close completed orders
    User can easily select the table and close the order which is paid.
6.  View your products selling statistics
    Statistics helps you analyze sales trends and optimize inventory and pricing.

## Technologies used
- Front end: HTML, CSS, JavaScript
- Back end: Flask, Python, JavaScript
- Database: SQL
- Libraries/Frameworks: Bootstrap, Jinja2, Werkzeug, SQLAlchemy
- Version control: Github
- Development Tools: Visual Studio Code

## How to Install
### Prerequisites
Before your begin, ensure that you have the following installed on your machine:

- Python
- pip 

### Steps
1. **Clone the repository**
    Clone the repository to your local machine using Git:
    ```bash
    git clone https://github.com/thanasisnik/final-project.git

2. **Navigate to the project folder**
    ```bash
    cd final-project

3. **Install the depedencies**
    ```bash
    pip install -r requirements.txt

4. **Optional** Set up a virtual environment to manage project depedencies. To create and activate a virtual environment run:
    
    - On Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

    - On Linux/macOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

5. **Run the application**
    - On windows:
    ```bash
    set FLASK_APP=app.py
    ```
    
    - On Linux/macOs
    ```bash
    export FLASK_APP=app.py
    ```
    - Run the Flask app:
    ```bash
    flask run

## How to use
1. After running the app with flask run, open a browser and go to `http://127.0.0.1:5000/`
2. Register and Log in to start managing the store by adding tables, products and creating orders

For more details on how each feature works, refer to **Features** section above.

## Code Documentation

Before diving into the code documentation, please refer to the Acknowledgments section for a summary of technologies i already know, what I learned during this Project, and how AI assists me to accomplish specific tasks. This will provide context for understanding the choices I made while developing ths application.

### app.py
The `app.py` file contains the main configuration and initialization of the Flask app including:
- **Flask app Setup**: Initializes the Flask app and configures it with `Config`
- **Database Initialization**: Connects to the database using SQLAlchemy
- **Route registration**: Registers all routes for the application from the `routes.py`
- **Session Management**: Uses Flask-Session for session handling.

### routes.py
The `routes.py` file containes the application routes including:
- `/`: This is the main route, where login is required to preview the features
- `/add_table`: A route the handles adding new tables
- `/add_product`: A route for adding new products to the menu
- `/order/<int:table_id>`: This route allows users to interact with the order system, adding products to a specific table ,identified by the table_id URL parameter, order and managing in real time. The ability to either create a new order or continue with an existing one makes this route essential for managing the orders.
- `/order/<int:table_id>/close`: A route to close the table's order again taking a URL parameter
- `/settings`: Route to change the theme from light to dark mode and also you can make a user password change.
-`/statistics`: This route provides a summarized view of product sales which is useful for tracking performance and understanding which products are selling the most. The database query aggregates the quanity of products sold by joining the Products table with the OrderItems table, where the product_id matched the id in the Products table. Then a sum function calculates the total quanity sold from the OrderItems table. We use a group_by "id" of the products ensuring that each product sales are aggregated. Finally a order_by to sort the products by the total quanity sold in descending order.
-`/register`: Route to register a User
- `/login`: A route where the registered User can login and start work with the application.
- `/logout`: User log out, clear the session( forger user_id)

### models.py 
In this file, we define our schema and models along with their relationships. These models represent the structure of the database and how diferent entities in the application interact with each other.
- Users model represents registered users in the application, storing ther login credentials ( username and a hashed password).
- Tables model represents the tables in the restaurant ensuring each table can have only one active order at a time.
- Orders model represents the orders placed at a table, each order can have multiple items. The status field tracks whether the order is active or no.
- Products model represents the products available for sale, storing their name and price.
- OrderItems model links products to orders, storing the quantity and price of each item in an order.

### templates/
Templates directory stores the HTML Files that render the front end of the application and built with using Jinja2 which allows us to dynamically inject content from our Python code into HTML (ex. database info).

### static/
Static directory contains all the static files such as CSS and JavaScript, that are used to style and add interactivity to the application.

## Acknowledgments

Since I already had experience with Flask from personal projects and CS50, I decided to create a web app to manage orders. For the database, I used SQLAlchemy, which required me to read the documentation and watch YouTube tutorials to fully understand it. About two days of the project were dedicated to this, as I already had the SQL logic down. For the front-end, I used HTML, CSS, Jinja2, Bootstrap, and JavaScript, which were technologies I had previously learned through an online course on Udemy and CS50. However, I encountered some errors in JavaScript that required AI assistance to resolve, though my focus was always on understanding the logic behind the solution. One such case was with Chart.js, which I found to be a great tool and might use again in the future. While I didn’t face major challenges in the back-end (Flask and Python), there were small issues I solved with help from Stack Overflow. In summary, this project taught me how to build a web app using HTML, CSS, JS (AI support), Flask, Python, and SQLAlchemy (documentation, YouTube tutorials, and some AI help).

## Future of the app

This project was implemented within a short time frame. Additional features, such as table reservations and product deletion, could be added in the future to complete the project and showcase my full skill set.


    