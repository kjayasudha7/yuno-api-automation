python
from behave import given, when, then
from utils.api_client import ApiClient
from utils.payload_builder import minimal_purchase_payload
from utils.config import BASE_URL
from utils.test_data_loader import load_cards

cards = load_cards()
VALID_CARD = cards["valid_card"]
EXPIRED_CARD = cards["expired_card"]

@given("an authorized payment exists")
def step_create_authorized_payment(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)
    payload["transaction_type"] = "AUTHORIZATION"
    context.response = ApiClient.post(url, context.headers, payload)

    assert context.response.status_code == 201
    response_json = context.response.json()

    assert response_json["status"] == "AUTHORIZED"
    context.authorization_id = response_json["id"]


@when("I create an authorization payment")
def step_create_authorization(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)
    payload["transaction_type"] = "AUTHORIZATION"

    context.response = ApiClient.post(url, context.headers, payload)


@when("I create an authorization payment using expired card")
def step_authorization_with_expired_card(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(EXPIRED_CARD)
    payload["transaction_type"] = "AUTHORIZATION"

    context.response = ApiClient.post(url, context.headers, payload)


@then('the payment status should be "AUTHORIZED"')
def step_verify_authorized(context):
    response_json = context.response.json()
    assert response_json["status"] == "AUTHORIZED"


