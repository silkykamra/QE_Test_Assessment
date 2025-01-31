import requests
import json
from behave import given, when, then

BASE_URL = "https://reqres.in"

@given('the API endpoint "{endpoint}" is available')
def step_given_api_endpoint(context, endpoint):
    context.endpoint = BASE_URL + endpoint

@when("I send a GET request to fetch user details")
def step_when_send_get_request(context):
    response = requests.get(context.endpoint)
    context.response = response

@then("the response status should be 200")
def step_then_check_status_200(context):
    assert context.response.status_code == 200, f"Expected 200 but got {context.response.status_code}"

@then("the response should contain user details with ID 2")
def step_then_validate_user_details(context):
    data = context.response.json()
    assert data["data"]["id"] == 2, "User ID does not match expected value"

@when('I send a POST request with user data "{name}" and "{job}"')
def step_when_send_post_request(context, name, job):
    payload = {"name": name, "job": job}
    response = requests.post(context.endpoint, json=payload)
    context.response = response
    context.request_payload = payload

@then("the response status should be 201")
def step_then_check_status_201(context):
    assert context.response.status_code == 201, f"Expected 201 but got {context.response.status_code}"

@then("the response should contain user details with the given name and job")
def step_then_validate_post_response(context):
    data = context.response.json()
    assert data["name"] == context.request_payload["name"], "Name mismatch"
    assert data["job"] == context.request_payload["job"], "Job mismatch"
