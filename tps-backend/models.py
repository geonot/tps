from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone # Python's datetime, not flask_sqlalchemy's
from flask_login import UserMixin

# Initialize SQLAlchemy instance here
# This instance will be further configured in app.py with db.init_app(app)
db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Relationship to ParkingPayment
    # 'payments' is how you'd access the payments from a User object: user_instance.payments
    # 'user' is the backref attribute on ParkingPayment: payment_instance.user
    payments = db.relationship('ParkingPayment', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class ParkingPayment(db.Model):
    __tablename__ = 'parking_payments' # Pluralized table name

    id = db.Column(db.Integer, primary_key=True)
    # user_id can be nullable if payments can be made by guests (not logged in)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True, index=True) # Added index
    license_plate = db.Column(db.String(20), nullable=False, index=True) # Added index
    lot_id = db.Column(db.String(50), nullable=False)
    payment_type = db.Column(db.String(50), nullable=False) # e.g., 'daily', 'hourly', 'permit_monthly'
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    currency = db.Column(db.String(10), nullable=False, default='USD')
    # Store external transaction ID from payment provider (e.g., PayPal, Stripe)
    external_transaction_id = db.Column(db.String(100), unique=True, nullable=True, index=True)
    status = db.Column(db.String(50), nullable=False, default='pending', index=True) # e.g., pending, completed, failed, refunded

    # Using timezone-aware UTC datetimes is generally recommended
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # The 'user' attribute is defined by the backref in User.payments relationship already.
    # If you need explicit control or a different naming, you can define it here too, but ensure it matches.
    # user = db.relationship('User', backref=db.backref('payments_alt', lazy=True)) # Example if backref wasn't enough

    def __repr__(self):
        return f'<ParkingPayment {self.id} - LP: {self.license_plate} - Status: {self.status}>'
