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
