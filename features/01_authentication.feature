gherkin
Feature: Authorization Payment API

  @sanity
  Scenario: Create authorization with minimal fields
    When I create an authorization payment
    Then the response status should be 201
    And the payment status should be "AUTHORIZED"

  @negative
  Scenario: Authorization fails with expired card
    When I create an authorization payment using expired card
    Then the response status should be 402

  #INVALID_AMOUNT (400)
  @negative 
  Scenario: Authorization fails with Invalid amount
    When I create a payment with invalid amount
    Then INVALID_AMOUNT error should be returned

#INVALID_TOKEN (401)
  @negative
    Scenario: Authorization fails with invalid token
      When I use an invalid token
      Then INVALID_TOKEN error should be returned

  #PAYMENT_NOT_FOUND (404)
  @negative
    Scenario: Authorization fails when paymnet not found
      When I fetch a payment with invalid id
      Then PAYMENT_NOT_FOUND error should be returned

  #IDEMPOTENCY_DUPLICATED (409)
  @negative
    Scenario: Authorization fails with idempotency duplicated
      When I reuse the same idempotency key
      Then IDEMPOTENCY_DUPLICATED error should be returned




      
