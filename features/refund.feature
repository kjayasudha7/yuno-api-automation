gherkin
Feature: Refund Payment

  @sanity
  Scenario: Refund a captured payment
    Given a captured payment exists
    When I refund the payment
    Then the refund status should be "SUCCEEDED"

  @negative
  Scenario: Refund with invalid payment ID
    When I refund a payment with invalid ID
    Then the response status should be 404
