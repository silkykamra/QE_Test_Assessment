Feature: Data Transformation Validation

  Scenario: Validate that output file has correct transformations
    Given input files are available
    When the application generates the output file
    Then output file should have correct transformations
