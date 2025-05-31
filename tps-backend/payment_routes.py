from flask import Blueprint, request, jsonify
# Corrected import for direct execution context (like auth_routes.py)
from models import db, ParkingPayment, User
from flask_login import current_user # login_required can be added if needed for specific routes
import uuid # For mock transaction IDs
from decimal import Decimal # For handling currency amounts precisely

payment_bp = Blueprint('payment_bp', __name__, url_prefix='/payment')

@payment_bp.route('/initiate', methods=['POST'])
def initiate_payment():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing data"}), 400

    license_plate = data.get('license_plate')
    lot_id = data.get('lot_id')
    payment_type = data.get('payment_type', 'daily') # Default to daily
    amount_str = data.get('amount')

    user_id = None
    if current_user.is_authenticated:
        user_id = current_user.id
    # else: # Allow guest payments, user_id remains None
        # For guest payments, might want to collect email or other identifier if needed for receipts
        # guest_email = data.get('guest_email')

    if not all([license_plate, lot_id, amount_str]):
        return jsonify({"error": "Missing required fields: license_plate, lot_id, amount"}), 400

    try:
        amount = Decimal(amount_str) # Validate and convert amount to Decimal
        if amount <= Decimal('0.00'):
            return jsonify({"error": "Amount must be positive"}), 400
    except Exception:
        return jsonify({"error": "Invalid amount format"}), 400

    try:
        new_payment = ParkingPayment(
            user_id=user_id,
            license_plate=license_plate,
            lot_id=lot_id,
            payment_type=payment_type,
            amount=amount,
            status='pending',
            currency='USD' # Default currency
        )
        db.session.add(new_payment)
        db.session.commit()

        mock_paypal_payment_id = f"MOCKPAY-{uuid.uuid4()}"
        mock_paypal_redirect_url = (
            # In a real app, this would be a URL to your frontend,
            # which then calls your backend's /success_callback or /cancel_callback
            # For now, let's pretend it's a direct link to a backend confirmation for simplicity of mocking.
            # Ideally, these would be frontend URLs.
            f"/api/payment/success_callback?internal_payment_id={new_payment.id}&token={mock_paypal_payment_id}"
            # Example: f"http://localhost:8080/payment/success?internal_payment_id={new_payment.id}..."
        )

        return jsonify({
            "message": "Payment initiated (mock)",
            "internal_payment_id": new_payment.id,
            "mock_paypal_payment_id": mock_paypal_payment_id,
            "redirect_url": mock_paypal_redirect_url
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Could not initiate payment processing.", "details": str(e)}), 500

@payment_bp.route('/success_callback', methods=['GET'])
def payment_success_callback():
    internal_payment_id = request.args.get('internal_payment_id')
    mock_provider_transaction_id = request.args.get('token') or f"MOCKTXN-{uuid.uuid4()}"

    if not internal_payment_id:
        return jsonify({"error": "Missing internal_payment_id from payment provider redirect"}), 400

    payment = ParkingPayment.query.get(internal_payment_id)
    if not payment:
        return jsonify({"error": "Payment record not found"}), 404

    if payment.status == 'completed':
        return jsonify({"message": "Payment already processed as completed", "internal_payment_id": payment.id}), 200

    try:
        payment.status = 'completed'
        payment.external_transaction_id = mock_provider_transaction_id
        db.session.commit()

        return jsonify({
            "message": "Payment successfully completed (mock)",
            "internal_payment_id": payment.id,
            "external_transaction_id": payment.external_transaction_id
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Payment completion processing failed.", "details": str(e)}), 500

@payment_bp.route('/cancel_callback', methods=['GET'])
def payment_cancel_callback():
    internal_payment_id = request.args.get('internal_payment_id')

    if not internal_payment_id:
        return jsonify({"error": "Missing internal_payment_id from payment provider redirect"}), 400

    payment = ParkingPayment.query.get(internal_payment_id)
    if not payment:
        return jsonify({"error": "Payment record not found"}), 404

    if payment.status == 'cancelled':
        return jsonify({"message": "Payment already processed as cancelled", "internal_payment_id": payment.id}), 200
    if payment.status == 'completed':
        return jsonify({"error": "Cannot cancel a payment that was already completed"}), 400

    try:
        payment.status = 'cancelled'
        db.session.commit()
        return jsonify({"message": "Payment cancelled (mock)", "internal_payment_id": payment.id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Payment cancellation processing failed.", "details": str(e)}), 500
