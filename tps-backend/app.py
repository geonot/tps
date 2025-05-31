from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_login import LoginManager
import os

# Import the db instance and User model from models.py
# ParkingPayment will also be available via 'models' if models.py is imported,
# or can be explicitly imported if needed by Flask-Migrate context here.
# For Flask-Migrate, ensuring 'db' knows about all models is key.
# Importing 'models' or specific models like User, ParkingPayment ensures they are registered with db.metadata.
from models import db, User, ParkingPayment

# Determine base directory for SQLite path
basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize Flask App
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_very_secret_key_that_should_be_changed_in_production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db) # db instance now knows about User and ParkingPayment

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login' # Refers to the 'login' function within the 'auth' blueprint

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import and register blueprints
from auth_routes import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from payment_routes import payment_bp
app.register_blueprint(payment_bp, url_prefix='/payment') # Default prefix is /payment as defined in blueprint itself

# Basic route for testing
@app.route('/')
def index():
    return jsonify({"message": "Welcome to Tacoma Parking Services API"}), 200

if __name__ == '__main__':
    app.run(debug=True)
