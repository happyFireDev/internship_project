
Feature: Testing the Add a project section under the settings menu

  Scenario: User can add a project through the settings
    Given Open the login page
    When Enter email
    And Enter password
    When Click login button
    Then Click on the settings option
    And Click on Add a project
    And Verify the right page opens
    And Add some test information to the input fields
    And Verify the correct information is present in the input fields
    And Verify the “Send an application” button is available and clickable