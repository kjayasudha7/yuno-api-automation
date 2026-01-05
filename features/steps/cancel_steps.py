python
from behave import given, when, then
from utils.api_client import ApiClient
from utils.payload_builder import minimal_purchase_payload
from utils.config import BASE_URL
from utils.test_data_loader import load_cards

cards = load_cards()
VALID_CARD = cards["valid_card"]
EXPIRED_CARD = cards["expired_card"]

@given("an authorized payment exists for cancellation")
def step_authorized_payment_for_cancel(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)
    payload["transaction_type"] = "AUTHORIZATION"

    context.response = ApiClient.post(url, context.headers, payload)
    assert context.response.status_code == 201

    response_json = context.response.json()
    assert response_json["status"] == "AUTHORIZED"

    context.authorization_id = response_json["id"]


@when("I cancel the authorized payment")
def step_cancel_authorized_payment(context):
    cancel_url = f"{BASE_URL}/payments/{context.authorization_id}/cancel"
    context.response = ApiClient.post(cancel_url, context.headers, {})


@then('the payment status should be "CANCELLED"')
def step_verify_cancel_status(context):
    response_json = context.response.json()
    assert response_json["status"] == "CANCELLED"


@when("I try to cancel a captured payment")
def step_cancel_captured_payment(context):
    # Step 1: Capture the authorization
    capture_url = f"{BASE_URL}/payments/{context.authorization_id}/capture"
    capture_response = ApiClient.post(capture_url, context.headers, {})
    assert capture_response.status_code == 201

    # Step 2: Try to cancel captured payment
    captured_id = capture_response.json()["id"]
    cancel_url = f"{BASE_URL}/payments/{captured_id}/cancel"
    context.response = ApiClient.post(cancel_url, context.headers, {})


---
