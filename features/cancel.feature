Feature: Cancel Payment

  @regression
  Scenario: Cancel authorized payment
    Given an authorized payment exists
    When I cancel the payment
    Then the payment status should be "CANCELLED"
