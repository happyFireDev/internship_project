
Feature: Testing the Add a project section under the settings menu

  Scenario: User can add a project through the settings
    Given Open the login page
    When Enter email
    And Enter password
    And Click login button
    Then Verify user is fully logged in
    When Click on the settings option
    And Click on Add a project
    Then Verify the right page opens
    When Add some test information to the input fields
    Then Verify the correct information is present in the input fields
    And Verify the “Send an application” button is available and clickable



#📌 Notes on Gherkin Formatting:
# Given sets up the initial context or state.
# When is for the primary action(s) being tested (usually a user action).
# Then is for expected outcomes or assertions.
# And is used to add additional steps under the same keyword as the line above.

