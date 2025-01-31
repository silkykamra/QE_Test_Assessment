Feature: API Testing for ReqRes

  Scenario: Get user by ID
    Given the API endpoint "/api/users/2" is available
    When I send a GET request to fetch user details
    Then the response status should be 200
    And the response should contain user details with ID 2

  Scenario: Create a new user
    Given the API endpoint "/api/users" is available
    When I send a POST request with user data "morpheus" and "leader"
    Then the response status should be 201
    And the response should contain user details with the given name and job