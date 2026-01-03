Feature: Verify Card

  @sanity
  Scenario: Verify card with valid details
    When I create a payment with verify true
    Then the response status should be 201
    And the verification result should be "VERIFIED"
