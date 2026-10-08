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

        print("\n===== DEBUG =====")
        print("URL:", url)
        print("Status Code:", response.status_code)
        print("Response:")
        print(response.text)
        print("=================\n")

        response.raise_for_status()

        return response.json()