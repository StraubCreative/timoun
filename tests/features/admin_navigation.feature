Feature: Testing the Navigation Bar
  Scenario: Make sure the navigation bar has the correct links
    Given I sign is as an admin user
      And I go to "http://localhost:8080/admin"
      When I click on "Users"
      Then I should see "Add User"
      When I click on "Organizations"
      Then I should see "Add Organization"
      When I click on "Services"
      Then I should see "Add Services"
      When I click on "Programs"
      Then I should see "Add Program"
      When I click on "Records"
      Then I should see "See Record History"
      When I click on "Manual"
      Then I should see "Timoun Manual"
      When I click on "Profile"
      Then I should see "Name"
      And I go to "http://localhost:8080/admin"
      When I click on "Dashboard"
      Then I should see "Initiated By"
      When I click on "Logout"
      Then I should see "Future Home"
