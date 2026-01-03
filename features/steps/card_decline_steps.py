python
from behave import when, then
from utils.api_client import ApiClient
from utils.payload_builder import minimal_purchase_payload
from utils.test_data_loader import load_cards
from utils.config import BASE_URL

cards = load_cards()

@when("I create a purchase payment using insufficient funds card")
def step_insufficient_funds_payment(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(cards["insufficient_funds_card"])
    context.response = ApiClient.post(url, context.headers, payload)

@when("I create a purchase payment using cvv mismatch card")
def step_cvv_mismatch_payment(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(cards["cvv_mismatch_card"])
    context.response = ApiClient.post(url, context.headers, payload)

@then('the error code should be "{expected_error_code}"')
def step_verify_error_code(context, expected_error_code):
    response_json = context.response.json()
    assert "error" in response_json
    assert response_json["error"]["code"] == expected_error_code
