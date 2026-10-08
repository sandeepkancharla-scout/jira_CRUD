from jira_client import JiraClient

jira = JiraClient()

issue_key = input(
    "Enter Jira Ticket ID: "
)

print("\nSupported Fields")
print("1. summary")
print("2. labels")

field_name = input(
    "\nEnter Field Name: "
)

field_value = input(
    "Enter New Value: "
)

# Special handling for labels
if field_name.lower() == "labels":

    field_value = [
        label.strip()
        for label in field_value.split(",")
    ]

try:

    jira.update_field(
        issue_key,
        field_name,
        field_value
    )

    print(
        f"\n {field_name} updated successfully"
    )

except Exception as e:

    print(
        f"\n Update failed: {e}"
    )