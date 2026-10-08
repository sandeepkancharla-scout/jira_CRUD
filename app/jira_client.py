import requests

from config import (
    JIRA_BASE_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN
)


class JiraClient:

    def __init__(self):

        self.auth = (
            JIRA_EMAIL,
            JIRA_API_TOKEN
        )

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def get_issue(self, issue_key):

        url = (
            f"{JIRA_BASE_URL}"
            f"/rest/api/3/issue/{issue_key}"
        )

        response = requests.get(
            url,
            headers=self.headers,
            auth=self.auth
        )

        response.raise_for_status()

        return response.json()

    def get_transitions(self, issue_key):

        url = (
            f"{JIRA_BASE_URL}"
            f"/rest/api/3/issue/{issue_key}/transitions"
        )

        response = requests.get(
            url,
            headers=self.headers,
            auth=self.auth
        )

        response.raise_for_status()

        return response.json()

    def change_status(
        self,
        issue_key,
        transition_id
    ):

        url = (
            f"{JIRA_BASE_URL}"
            f"/rest/api/3/issue/{issue_key}/transitions"
        )

        payload = {
            "transition": {
                "id": transition_id
            }
        }

        response = requests.post(
            url,
            headers=self.headers,
            auth=self.auth,
            json=payload
        )

        response.raise_for_status()

        return True
    def get_editable_fields(self, issue_key):

        url = (
            f"{JIRA_BASE_URL}"
            f"/rest/api/3/issue/{issue_key}/editmeta"
        )

        response = requests.get(
            url,
            headers=self.headers,
            auth=self.auth
        )

        response.raise_for_status()

        return response.json()


    def update_field(
        self,
        issue_key,
        field_name,
        field_value
    ):

        url = (
            f"{JIRA_BASE_URL}"
            f"/rest/api/3/issue/{issue_key}"
        )

        payload = {
            "fields": {
                field_name: field_value
            }
        }

        response = requests.put(
            url,
            headers=self.headers,
            auth=self.auth,
            json=payload
        )

        print("Status Code:", response.status_code)

        if response.text:
            print(response.text)

        response.raise_for_status()

        return True

    def test_connection(self):

        url = (
            f"{JIRA_BASE_URL}"
            f"/rest/api/3/myself"
        )

        response = requests.get(
            url,
            headers=self.headers,
            auth=self.auth
        )

        response.raise_for_status()

        return response.json()