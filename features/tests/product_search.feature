Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown


  Scenario: User can add a project through the settings
    Given Open the main page https://soft.reelly.io/sign-in
    When Log in to the page
    And Click on the settings option
    And Click on Add a project
    And Verify the right page opens
    And Add some test information to the input fields
    Then Verify the right information is present in the input fields
    And Verify the “Send an application” button is available and clickable