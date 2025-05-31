from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

# Changed from ".models" to "models" for simpler direct import
# as app.py, auth_routes.py, and models.py are in the same directory (tps-backend)
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing username, email, or password"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 409
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 409

    new_user = User(username=username, email=email)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully", "user": {"id": new_user.id, "username": new_user.username, "email": new_user.email}}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email_or_username = data.get('email_or_username')
    password = data.get('password')

    if not email_or_username or not password:
        return jsonify({"error": "Missing email/username or password"}), 400

    user = User.query.filter((User.email == email_or_username) | (User.username == email_or_username)).first()

    if user and user.check_password(password):
        login_user(user) # `remember=True` can be added
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email
            }
        }), 200

    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200

@auth_bp.route('/profile', methods=['GET'])
@login_required
def profile():
    return jsonify({
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "created_at": current_user.created_at.isoformat()
    }), 200
