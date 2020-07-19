import json
import uuid
from http import HTTPStatus
from os import getenv

import requests
from behave import *

api_token = getenv("apitoken")


@step("I create a project with name {name}")
def create_project(context, name):
    context.expected_project_name = name
    response = requests.post(
        "https://api.todoist.com/rest/v1/projects",
        data=json.dumps({
            "name": name
        }),
        headers={
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": f"Bearer {api_token}"
        }).json()
    context.project_id = response["id"]


@step("I update project name to {name}")
def update_project_name(context, name):
    context.expected_project_name = name
    requests.post(
        f"https://api.todoist.com/rest/v1/projects/{context.project_id}",
        data=json.dumps({
            "name": name
        }),
        headers={
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": f"Bearer {api_token}"
        })


@step("I get project details")
def get_project_details(context):
    response = requests.get(
        f"https://api.todoist.com/rest/v1/projects/{context.project_id}",
        headers={"Authorization": f"Bearer {api_token}"}
    ).json()
    context.project_details = response


@step("I verify project has correct name")
def verify_project_name(context):
    assert context.project_details["name"] == context.expected_project_name, \
        f"Project name is {context.project_name}, but should be {context.expected_project_name}"


@step("I delete created project")
def delete_project(context):
    requests.delete(
        f"https://api.todoist.com/rest/v1/projects/{context.project_id}",
        headers={"Authorization": f"Bearer {api_token}"}
    )


@step("I verify that project is no longer exists")
def verify_project_is_deleted(context):
    response = requests.get(
        f"https://api.todoist.com/rest/v1/projects/{context.project_id}",
        headers={"Authorization": f"Bearer {api_token}"}
    )
    assert response.status_code == HTTPStatus.NOT_FOUND, f"Expected status is 404 but was {response.status_code}"
