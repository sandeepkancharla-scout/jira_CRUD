from jira_client import JiraClient

jira = JiraClient()

issue_key = input(
    "Enter Jira Ticket ID: "
)

try:

    issue = jira.get_issue(issue_key)

    fields = issue["fields"]

    validation_errors = []

    if not fields.get("summary"):
        validation_errors.append(
            "Summary is missing"
        )

    if not fields.get("status"):
        validation_errors.append(
            "Status is missing"
        )

    if not fields.get("priority"):
        validation_errors.append(
            "Priority is missing"
        )

    if not fields.get("assignee"):
        validation_errors.append(
            "Assignee is missing"
        )

    print("\n===== VALIDATION RESULTS =====")

    if validation_errors:

        print("Validation Failed\n")

        for error in validation_errors:
            print(f" {error}")

    else:

        print("Validation Passed")

        print(f"Ticket : {issue_key}")
        print(
            f"Status : "
            f"{fields['status']['name']}"
        )

except Exception as e:

    print(
        f"Validation Error: {e}"
    )