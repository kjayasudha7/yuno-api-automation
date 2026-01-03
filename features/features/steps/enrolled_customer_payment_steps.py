python
from behave import given, when, then
from utils.api_client import ApiClient
from utils.test_data_loader import load_customers, load_cards
from utils.config import BASE_URL

customers = load_customers()
cards = load_cards()

@given("a customer exists")
def step_create_customer(context):
    payload = customers["minimal_customer"].copy()
    payload["account_id"] = "to_complete"

    url = f"{BASE_URL}/customers"
    context.response = ApiClient.post(url, context.headers, payload)

    assert context.response.status_code == 201
    context.customer_id = context.response.json()["id"]

@given("the customer has an enrolled card payment method")
def step_enroll_card(context):
    enroll_url = f"{BASE_URL}/payment-methods/enroll"

    payload = {
        "account_id": "to_complete",
        "customer_id": context.customer_id,
        "payment_method": {
            "type": "CARD",
            "card": cards["valid_card"]
        }
    }

    context.response = ApiClient.post(enroll_url, context.headers, payload)

    assert context.response.status_code == 201
    context.payment_method_id = context.response.json()["id"]

@when("I create a purchase payment using enrolled customer")
def step_purchase_with_enrolled_customer(context):
    payment_url = f"{BASE_URL}/payments"

    payload = {
        "account_id": "to_complete",
        "amount": 1000,
        "currency": "USD",
        "workflow": "DIRECT",
        "customer": {
            "id": context.customer_id
        }
    }

    context.response = ApiClient.post(payment_url, context.headers, payload)

@then('the payment status should be "{expected_status}"')
def step_verify_payment_status(context, expected_status):
    response_json = context.response.json()
    assert response_json["status"] == expected_status

