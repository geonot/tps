from flask import Blueprint, jsonify
from models import User, db # Corrected to direct import for consistency with other route files
# from flask_login import login_required, current_user # For actual authentication/authorization

admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')

@admin_bp.route('/users', methods=['GET'])
# @login_required # This should be enabled in a real application
def list_users():
    # In a real app, you would also check if current_user is an admin:
    # if not current_user.is_admin_role(): # Assuming an is_admin_role() method or attribute
    # return jsonify({"error": "Unauthorized access"}), 403

    try:
        users = User.query.all()
        user_list = [{
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at.isoformat() if user.created_at else None
        } for user in users]
        return jsonify(user_list), 200
    except Exception as e:
        # Log the exception e for server-side debugging
        return jsonify({"error": "Failed to retrieve users.", "details": str(e)}), 500
