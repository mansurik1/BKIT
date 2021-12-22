Feature: Testing the function get_roots
  Scenario: Get roots of biquadratic equation for coefficients [-4, 16, 0]
    Given I put coefficients [-4, 16, 0] into the function
    Then I get roots [-0.0, 4.0]

Scenario: Get roots of biquadratic equation for coefficients [1, 1, -2]
  Given I put coefficients [1, 1, -2] into the function
  Then I get roots [1.0, -2.0]

Scenario: Get roots of biquadratic equation for coefficients [1, 1, 1]
  Given I put coefficients [1, 1, 1] into the function
  Then I get roots []
