from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_login import LoginManager
import os

from models import db, User, ParkingPayment

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_very_secret_key_that_should_be_changed_in_production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Import and register blueprints
from auth_routes import auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from payment_routes import payment_bp
app.register_blueprint(payment_bp) # url_prefix is '/payment' in blueprint

from qr_code_routes import qr_code_bp
app.register_blueprint(qr_code_bp) # url_prefix is '/qr' in blueprint

from admin_routes import admin_bp
app.register_blueprint(admin_bp) # url_prefix is '/admin' in blueprint


@app.route('/')
def index():
    return jsonify({"message": "Welcome to Tacoma Parking Services API"}), 200

if __name__ == '__main__':
    app.run(debug=True)
