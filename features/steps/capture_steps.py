python
from behave import given, when, then
from utils.api_client import ApiClient
from utils.payload_builder import minimal_purchase_payload
from utils.config import BASE_URL
from utils.test_data_loader import load_cards

cards = load_cards()
VALID_CARD = cards["valid_card"]
EXPIRED_CARD = cards["expired_card"]

@given("an authorized payment exists for capture")
def step_authorized_payment_for_capture(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)
    payload["transaction_type"] = "AUTHORIZATION"

    context.response = ApiClient.post(url, context.headers, payload)
    assert context.response.status_code == 201

    response_json = context.response.json()
    assert response_json["status"] == "AUTHORIZED"

    context.authorization_id = response_json["id"]

@when("I capture the authorized payment")
def step_capture_authorization(context):
    capture_url = f"{BASE_URL}/payments/{context.authorization_id}/capture"
    context.response = ApiClient.post(capture_url, context.headers, {})

@then('the payment status should be "CAPTURED"')
def step_verify_capture_status(context):
    response_json = context.response.json()
    assert response_json["status"] == "CAPTURED"
    context.payment_id = response_json["id"]

@when("I try to capture a payment without authorization")
def step_capture_without_authorization(context):
    capture_url = f"{BASE_URL}/payments/invalid-auth-id/capture"
    context.response = ApiClient.post(capture_url, context.headers, {})

