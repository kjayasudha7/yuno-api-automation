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

@Then("the response status should be 201")
def response_status_201(context):
     url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)
    payload["transaction_type"] = "AUTHORIZATION"
    context.response = ApiClient.post(url, context.headers, payload)

    assert context.response.status_code == 201
    response_json = context.response.json()


@then('the payment status should be "AUTHORIZED"')
def step_verify_authorized(context):
    response_json = context.response.json()
    assert response_json["status"] == "AUTHORIZED"


@when("I create an authorization payment using expired card")
def step_authorization_with_expired_card(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(EXPIRED_CARD)
    payload["transaction_type"] = "AUTHORIZATION"

    context.response = ApiClient.post(url, context.headers, payload)


@Then("the response status should be 402")
def response_status_201(context):
     url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)
    payload["transaction_type"] = "AUTHORIZATION"
    context.response = ApiClient.post(url, context.headers, payload)

    assert context.response.status_code == 402
    response_json = context.response.json()


#INVALID_AMOUNT (400)
@when("I create a payment with invalid amount")
def step_invalid_amount(context):
    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)
    payload["amount"] = -100  # Invalid

    context.response = ApiClient.post(url, context.headers, payload)

@then("INVALID_AMOUNT error should be returned")
def step_validate_invalid_amount(context):
    validate_error_response(
        response=context.response,
        expected_status=400,
        expected_code=ErrorCodes.INVALID_AMOUNT
    )

#INVALID_TOKEN (401)
@when("I use an invalid token")
def step_invalid_token(context):
    context.headers["Authorization"] = "Bearer invalid_token"

    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)
    context.response = ApiClient.post(url, context.headers, payload)

@then("INVALID_TOKEN error should be returned")
def step_validate_invalid_token(context):
    validate_error_response(
        context.response,
        401,
        ErrorCodes.INVALID_TOKEN
    )

#PAYMENT_NOT_FOUND (404)
@when("I fetch a payment with invalid id")
def step_payment_not_found(context):
    url = f"{BASE_URL}/payments/invalid_id"
    context.response = ApiClient.get(url, context.headers)


@then("PAYMENT_NOT_FOUND error should be returned")
def step_validate_payment_not_found(context):
    validate_error_response(
        context.response,
        404,
        ErrorCodes.PAYMENT_NOT_FOUND
    )

#IDEMPOTENCY_DUPLICATED (409)
@when("I reuse the same idempotency key")
def step_duplicate_idempotency(context):
    headers = context.headers.copy()
    headers["Idempotency-Key"] = "duplicate-key"

    url = f"{BASE_URL}/payments"
    payload = minimal_purchase_payload(VALID_CARD)

    ApiClient.post(url, headers, payload)  # first call
    context.response = ApiClient.post(url, headers, payload)  # duplicate


@then("IDEMPOTENCY_DUPLICATED error should be returned")
def step_validate_idempotency(context):
    validate_error_response(
        context.response,
        409,
        ErrorCodes.IDEMPOTENCY_DUPLICATED
    )





