gherkin
Feature: Payment using enrolled customer payment method

  As a merchant
  I want to charge customers using enrolled payment methods
  So that customers do not need to re-enter card details

  Background:
    Given the payment API base URL is configured
    And valid authentication headers are generated

  @integration @sanity
  Scenario: Successful purchase using enrolled customer card
    Given a customer exists
    And the customer has an enrolled card payment method
    When I create a purchase payment using enrolled customer
    Then the response status should be 201
    And the payment status should be "SUCCEEDED"

  @negative @integration
  Scenario: Fail purchase using customer without enrolled card
    Given a customer exists
    When I create a purchase payment using enrolled customer
    Then the response status should be 400
    And the error message should contain "payment method not enrolled"

