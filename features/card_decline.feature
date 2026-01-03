gherkin
Feature: Card Decline Scenarios

  As a payment orchestrator
  I want to handle card decline scenarios correctly
  So that merchants receive proper error responses

  Background:
    Given the payment API base URL is configured
    And valid authentication headers are generated

  @negative @regression
  Scenario: Purchase fails due to insufficient funds
    When I create a purchase payment using insufficient funds card
    Then the response status should be 402
    And the error code should be "INSUFFICIENT_FUNDS"

  @negative @regression
  Scenario: Purchase fails due to CVV mismatch
    When I create a purchase payment using cvv mismatch card
    Then the response status should be 402
    And the error code should be "CVV_MISMATCH"
