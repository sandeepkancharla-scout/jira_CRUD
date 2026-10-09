import os

from jira_client import JiraClient

jira = JiraClient()

ticket_id = os.getenv(
    "TICKET_ID"
)

operation = os.getenv(
    "OPERATION"
)

field_name = os.getenv(
    "FIELD_NAME"
)

field_value = os.getenv(
    "FIELD_VALUE"
)

print(
    f"Ticket: {ticket_id}"
)

print(
    f"Operation: {operation}"
)


if operation == "read":

    issue = jira.get_issue(
        ticket_id
    )

    print(
        "\n===== TICKET DETAILS ====="
    )

    print(
        f"Key: {issue['key']}"
    )

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

    issue = jira.get_issue(
        ticket_id
    )

    fields = issue["fields"]

    validation_errors = []

    if not fields.get(
        "summary"
    ):
        validation_errors.append(
            "Summary Missing"
        )

    if not fields.get(
        "priority"
    ):
        validation_errors.append(
            "Priority Missing"
        )

    if not fields.get(
        "assignee"
    ):
        validation_errors.append(
            "Assignee Missing"
        )

    if validation_errors:

        print(
            "\nValidation Failed"
        )

        for error in (
            validation_errors
        ):

            print(
                f"- {error}"
            )

    else:

        print(
            "\nValidation Passed"
        )

elif operation == "get_fields":

    metadata = (
        jira.get_editable_fields(
            ticket_id
        )
    )

    print(
        "\n===== EDITABLE FIELDS ====="
    )

    for key, value in metadata[
        "fields"
    ].items():

        schema = value.get(
            "schema",
            {}
        )

        field_type = schema.get(
            "type",
            "unknown"
        )

        print(
            f"{key:<25}"
            f"| {value['name']:<30}"
            f"| {field_type}"
        )

elif operation == "status":

    issue = jira.get_issue(
        ticket_id
    )

    current_status = (
        issue["fields"]
        ["status"]["name"]
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

    available_transitions = []

    for transition in transitions[
        "transitions"
    ]:

        available_transitions.append(
            transition["name"]
        )

        print(
            f"{transition['id']} "
            f"-> "
            f"{transition['name']}"
        )

    if not field_value:

        print(
            "\nNo target status supplied."
        )

        print(
            "Run workflow again and provide "
            "FIELD_VALUE."
        )

        exit(0)

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
            f"Invalid status."
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

    print(
        "\n✅ STATUS UPDATED"
    )

    print(
        f"Old Status: "
        f"{current_status}"
    )

    print(
        f"New Status: "
        f"{updated_issue['fields']['status']['name']}"
    )

elif operation == "update":

    print(
        "\nUpdate operation "
        "will be implemented next."
    )

else:

    raise Exception(
        "Invalid operation."
    )