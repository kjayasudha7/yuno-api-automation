Feature: Customer and Payment Method Management

  #As a merchant, I want to create customers and enroll payment methods
  #So that payments can be made using saved customer details

  Background:
    Given the payment API base URL is configured
    And valid authentication headers are generated

  @sanity
  Scenario: Create customer with minimal required fields
    When I create a customer with minimal details
    Then the response status should be 201
    And the customer id should be present in the response

  @regression
  Scenario: Create customer with full details
    When I create a customer with full details
    Then the response status should be 201
    And the customer email should match the request

  @negative @regression
  Scenario: Fail to create customer without mandatory fields
    When I create a customer without required fields
    Then the response status should be 400
    And the error message should contain "missing required field"

  @sanity
  Scenario: Enroll card payment method for an existing customer
    Given a customer already exists
    When I enroll a card payment method for the customer
    Then the response status should be 201
    And the payment method status should be "ENROLLED"

  @negative @regression
  Scenario: Fail to enroll payment method with invalid card
    Given a customer already exists
    When I enroll a payment method using an invalid card
    Then the response status should be 400
    And the error code should be "INVALID_CARD"

  @integration @regression
  Scenario: Create payment using enrolled customer payment method
    Given a customer with enrolled payment method exists
    When I create a purchase payment using the customer payment method
    Then the response status should be 201
    And the payment status should be "SUCCEEDED"

  @negative @integration
  Scenario: Fail payment using non-enrolled payment method
    Given a customer exists without enrolled payment method
    When I create a payment using the customer payment method
    Then the response status should be 400
    And the error message should contain "payment method not enrolled"
