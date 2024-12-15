from flask import Flask
from flask_session import Session
from config import Config
from models import db, OrderItems
from routes import register_routes
from werkzeug.security import check_password_hash, generate_password_hash

#make a new Flask app
app = Flask(__name__)

#Loading the configuration of the app from Config class
app.config.from_object(Config)

#Initialize sqlalchemy from models to Flask, init_app connect them
db.init_app(app)

Session(app)

#insert all routes for the app 
register_routes(app)


with app.app_context():
    
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)