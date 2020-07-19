@projects
Feature: Projects API

  Scenario: Create a project and get details
    Given I create a project with name My New Project
    When I get project details
    Then I verify project has correct name

  Scenario: Update project name and check it is updated
    Given I create a project with name Old Project Name
    When I update project name to New Project Name
    And I get project details
    Then I verify project has correct name

  Scenario: Delete a project
    Given I create a project with name Project To Delete
    When I delete created project
    Then I verify that project is no longer exists
    