from flask import Blueprint, request, jsonify
import os # For FRONTEND_BASE_URL

qr_code_bp = Blueprint('qr_code_bp', __name__, url_prefix='/qr')

# In a real app, this would come from config or environment variables
# Consider making this configurable via app.config
FRONTEND_BASE_URL = os.environ.get('FRONTEND_BASE_URL', 'http://localhost:8080')

@qr_code_bp.route('/generate_link_data', methods=['POST'])
def generate_link_data():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing data"}), 400

    lot_id = data.get('lot_id')
    amount_str = data.get('amount') # Amount might come as string or number
    payment_type = data.get('payment_type', 'daily') # Default to daily

    if not lot_id or amount_str is None: # Amount can be 0, so check for None
        return jsonify({"error": "Missing required fields: lot_id, amount"}), 400

    try:
        # Validate amount format (e.g., ensure it's a number, optional: check for positive)
        amount = float(amount_str)
        if amount < 0: # Typically amounts should be non-negative
             return jsonify({"error": "Amount cannot be negative"}), 400
    except ValueError:
        return jsonify({"error": "Invalid amount format, must be a number"}), 400


    try:
        # Construct the URL for the frontend payment page (/pay)
        # Example: http://localhost:8080/pay?lot_id=LOT-A1&amount=5.00&payment_type=daily
        query_params = f"lot_id={lot_id}&amount={amount:.2f}&payment_type={payment_type}"
        target_url = f"{FRONTEND_BASE_URL}/pay?{query_params}"

        return jsonify({
            "message": "QR code link data generated successfully.",
            "target_url": target_url,
            "suggested_qr_content": target_url # This is what would be encoded in the QR
        }), 200
    except Exception as e:
        # Log the exception e for server-side debugging
        return jsonify({"error": "Failed to generate QR link data.", "details": str(e)}), 500
