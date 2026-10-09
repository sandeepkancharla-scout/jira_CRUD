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

    print("\n===== TICKET DETAILS =====")

    print(f"Key: {issue['key']}")

    print(
        f"Summary: "
        f"{issue['fields']['summary']}"
    )

    print(
        f"Status: "
        f"{issue['fields']['status']['name']}"
    )

    priority = issue["fields"].get(
        "priority"
    )

    assignee = issue["fields"].get(
        "assignee"
    )

    labels = issue["fields"].get(
        "labels",
        []
    )

    print(
        f"Priority: "
        f"{priority['name'] if priority else 'Not Set'}"
    )

    print(
        f"Assignee: "
        f"{assignee['displayName'] if assignee else 'Unassigned'}"
    )

    print(
        f"Labels: "
        f"{', '.join(labels) if labels else 'None'}"
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

    if not field_value:

        raise ValueError(
            "FIELD_VALUE is required."
        )

    issue = jira.get_issue(ticket_id)

    current_status = (
        issue["fields"]["status"]["name"]
    )

    print(
        f"\nCurrent Status: "
        f"{current_status}"
    )

    transitions = (
        jira.get_transitions(
            ticket_id
        )
    )

    print(
        "\n===== AVAILABLE TRANSITIONS ====="
    )

    transition_id = None

    for transition in transitions[
        "transitions"
    ]:

        print(
            f"{transition['id']} "
            f"-> "
            f"{transition['name']}"
        )

        if (
            transition["name"]
            .lower()
            ==
            field_value.lower()
        ):

            transition_id = (
                transition["id"]
            )

    if not transition_id:

        raise Exception(
            f"Transition "
            f"'{field_value}' "
            f"is not available."
        )

    jira.change_status(
        ticket_id,
        transition_id
    )

    updated_issue = (
        jira.get_issue(
            ticket_id
        )
    )

    new_status = (
        updated_issue["fields"]
        ["status"]["name"]
    )

    print(
        f"\n✅ Status Updated"
    )

    print(
        f"Old Status: "
        f"{current_status}"
    )

    print(
        f"New Status: "
        f"{new_status}"
    )