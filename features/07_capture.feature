gherkin
Feature: Capture Authorized Payment

  @sanity
  Scenario: Capture authorized payment successfully
    Given an authorized payment exists
    When I capture the authorization
    Then the response status should be 201
    And the payment status should be "CAPTURED"
