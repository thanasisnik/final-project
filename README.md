# final-project
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
    -On Windows:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate```

    -On Linux/macOS:
    ```bash
    python3 -m venv venv
    source venv/bin/activate```

5. **Run the application**
    - On windows:
    ```bash
    set FLASK_APP=app.py
    
    - On Linux/macOs
    ```bash
    export FLASK_APP=app.py

    - Run the Flask app:
    ```bash
    flask run