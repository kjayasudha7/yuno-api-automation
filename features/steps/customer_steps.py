python
from behave import given, when, then
from utils.api_client import ApiClient
from utils.test_data_loader import load_customers
from utils.config import BASE_URL

customers = load_customers()

@given("the payment API base URL is configured")
def step_base_url(context):
    context.base_url = BASE_URL


@when("I create a customer with minimal details")
def step_create_minimal_customer(context):
    payload = customers["minimal_customer"].copy()
    payload["account_id"] = "to_complete"

    url = f"{context.base_url}/customers"
    context.response = ApiClient.post(url, context.headers, payload)


@when("I create a customer with full details")
def step_create_full_customer(context):
    payload = customers["full_customer"].copy()
    payload["account_id"] = "to_complete"

    url = f"{context.base_url}/customers"
    context.response = ApiClient.post(url, context.headers, payload)


@when("I create a customer without required fields")
def step_create_invalid_customer(context):
    payload = customers["invalid_customer"].copy()
    payload["account_id"] = "to_complete"

    url = f"{context.base_url}/customers"
    context.response = ApiClient.post(url, context.headers, payload)


@then("the customer id should be present in the response")
def step_verify_customer_id(context):
    response_json = context.response.json()
    assert "id" in response_json
    context.customer_id = response_json["id"]
