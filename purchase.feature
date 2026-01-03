Feature: Purchase Payment API

  Background:
    Given the payment API base URL is configured
    And valid authentication headers are generated

  @sanity @regression
  Scenario: Create purchase payment with minimal fields
    When I create a purchase payment with minimal required fields
    Then the response status should be 201
    And the payment status should be "SUCCEEDED"

  @regression
  Scenario: Create purchase payment with maximal fields
    When I create a purchase payment with customer and additional data
    Then the response status should be 201
    And the payment status should be "SUCCEEDED"

  @negative @regression
  Scenario: Fail purchase payment with invalid card number
    When I create a purchase payment with invalid card details
    Then the response status should be 400
    And the error code should be "INVALID_CARD"

  @negative @regression
  Scenario: Fail purchase payment without workflow field
    When I create a purchase payment without workflow
    Then the response status should be 400
    And the error message should contain "workflow is required"

