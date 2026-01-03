python
from behave import given, when, then
from utils.api_client import ApiClient
from utils.payload_builder import minimal_purchase_payload
from utils.config import BASE_URL
from utils.test_data_loader import load_cards

cards = load_cards()
VALID_CARD = cards["valid_card"]
EXPIRED_CARD = cards["expired_card"]

@given("a captured payment exists")
def step_create_captured_payment(context):
    # Step 1: Create authorization
    auth_url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)
    payload["transaction_type"] = "AUTHORIZATION"

    auth_response = ApiClient.post(auth_url, context.headers, payload)
    assert auth_response.status_code == 201

    auth_json = auth_response.json()
    authorization_id = auth_json["id"]

    # Step 2: Capture authorization
    capture_url = f"{BASE_URL}/payments/{authorization_id}/capture"
    capture_response = ApiClient.post(capture_url, context.headers, {})

    assert capture_response.status_code == 201
    capture_json = capture_response.json()
    assert capture_json["status"] == "CAPTURED"

    context.payment_id = capture_json["id"]

@when("I refund the payment")
def step_refund_payment(context):
    refund_url = f"{BASE_URL}/payments/{context.payment_id}/refund"
    context.response = ApiClient.post(refund_url, context.headers, {})

@when("I refund a payment with invalid ID")
def step_refund_invalid_payment(context):
    refund_url = f"{BASE_URL}/payments/invalid-payment-id/refund"
    context.response = ApiClient.post(refund_url, context.headers, {})

@then('the refund status should be "SUCCEEDED"')
def step_verify_refund_status(context):
    response_json = context.response.json()
    assert response_json["status"] == "SUCCEEDED"
