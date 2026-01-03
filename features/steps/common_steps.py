python
from behave import given, when, then
from utils.api_client import ApiClient
from utils.payload_builder import minimal_customer_payload
from utils.config import BASE_URL

@given("the payment API base URL is configured")
def step_base_url(context):
    context.base_url = BASE_URL

@when("I create a customer with minimal details")
def step_create_customer(context):
    url = f"{context.base_url}/customers"
    payload = minimal_customer_payload()
    context.response = ApiClient.post(url, context.headers, payload)

@then("the response status should be {status_code:d}")
def step_verify_status(context, status_code):
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"

@then("the customer id should be present in the response")
def step_verify_customer_id(context):
    response_json = context.response.json()
    assert "id" in response_json
    context.customer_id = response_json["id"]
