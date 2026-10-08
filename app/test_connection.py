import requests

from config import (
    JIRA_BASE_URL,
    JIRA_EMAIL,
    JIRA_API_TOKEN
)

print("\n===== CONFIG =====")
print("URL:", JIRA_BASE_URL)
print("EMAIL:", JIRA_EMAIL)
print("TOKEN EXISTS:", bool(JIRA_API_TOKEN))
print("==================\n")

url = f"{JIRA_BASE_URL}/rest/api/3/myself"

response = requests.get(
    url,
    auth=(JIRA_EMAIL, JIRA_API_TOKEN)
)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)