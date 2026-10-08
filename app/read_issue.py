from jira_client import JiraClient

jira = JiraClient()

from config import *

print("URL:", JIRA_BASE_URL)
print("Email:", JIRA_EMAIL)
print("Token Exists:", bool(JIRA_API_TOKEN))

issue_key = input(
    "Enter Jira Ticket ID: "
)

issue = jira.get_issue(issue_key)

print("\n===== JIRA TICKET =====")

print(
    f"Key: {issue['key']}"
)

print(
    f"Summary: {issue['fields']['summary']}"
)

print(
    f"Status: {issue['fields']['status']['name']}"
)

priority = issue["fields"].get("priority")

print(
    f"Priority: {priority['name'] if priority else 'Not Set'}"
)

assignee = issue["fields"].get("assignee")

print(
    f"Assignee: {assignee['displayName'] if assignee else 'Unassigned'}"
)
