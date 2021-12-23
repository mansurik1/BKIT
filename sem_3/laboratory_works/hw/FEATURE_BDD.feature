Feature: Testing the function get_mod from main
  Scenario: Find the remainder of 14 divided by 13
    Given I put values [14, 13] into the function
    Then I get 1

Scenario: Find the remainder of 121 divided by 2
  Given I put values [121, 2] into the function
  Then I get 1

Scenario: Find the remainder of 21 divided by 9
  Given I put values [21, 9] into the function
  Then I get 3
