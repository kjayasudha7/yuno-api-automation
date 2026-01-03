python
from behave import when, then
from utils.api_client import ApiClient
from utils.payload_builder import minimal_purchase_payload
from utils.config import BASE_URL
from utils.test_data_loader import load_cards

cards = load_cards()
VALID_CARD = cards["valid_card"]
EXPIRED_CARD = cards["expired_card"]
INVALID_CARD = cards["invalid_card"]

@when("I create a purchase payment with minimal required fields")
def step_create_purchase(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)
    context.response = ApiClient.post(url, context.headers, payload)

@when("I create a purchase payment with invalid card details")
def step_create_invalid_purchase(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(INVALID_CARD)
    context.response = ApiClient.post(url, context.headers, payload)

@then('the payment status should be "{expected_status}"')
def step_verify_payment_status(context, expected_status):
    response_json = context.response.json()
    assert response_json["status"] == expected_status
