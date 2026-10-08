import os

from jira_client import JiraClient

jira = JiraClient()

ticket_id = os.getenv("TICKET_ID")
operation = os.getenv("OPERATION")
field_name = os.getenv("FIELD_NAME")
field_value = os.getenv("FIELD_VALUE")

print(f"Ticket: {ticket_id}")
print(f"Operation: {operation}")

if operation == "read":

    issue = jira.get_issue(ticket_id)

    print("\nTicket Details")

    print(
        f"Summary: "
        f"{issue['fields']['summary']}"
    )

    print(
        f"Status: "
        f"{issue['fields']['status']['name']}"
    )

elif operation == "validate":

    issue = jira.get_issue(ticket_id)

    fields = issue["fields"]

    errors = []

    if not fields.get("summary"):
        errors.append("Summary Missing")

    if not fields.get("priority"):
        errors.append("Priority Missing")

    if not fields.get("assignee"):
        errors.append("Assignee Missing")

    if errors:

        print("Validation Failed")

        for error in errors:
            print(error)

    else:

        print("Validation Passed")

elif operation == "get_fields":

    metadata = (
        jira.get_editable_fields(ticket_id)
    )

    print("\nEditable Fields")

    for key, value in metadata[
        "fields"
    ].items():

        print(
            f"{key} -> "
            f"{value['name']}"
        )

elif operation == "update":

    jira.update_field(
        ticket_id,
        field_name,
        field_value
    )

    print(
        f"{field_name} updated successfully"
    )

elif operation == "status":

    transitions = (
        jira.get_transitions(ticket_id)
    )

    transition_id = None

    for transition in transitions[
        "transitions"
    ]:

        if (
            transition["name"]
            .lower()
            ==
            field_value.lower()
        ):

            transition_id = (
                transition["id"]
            )

            break

    if not transition_id:

        raise Exception(
            f"Status "
            f"{field_value} "
            f"not found"
        )

    jira.change_status(
        ticket_id,
        transition_id
    )

    print(
        f"Status changed to "
        f"{field_value}"
    )