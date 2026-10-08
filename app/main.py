from jira_client import JiraClient

jira = JiraClient()

while True:

    print("\n===== JIRA CRUD APPLICATION =====")
    print("1. Read Ticket")
    print("2. Validate Ticket")
    print("3. Update Field")
    print("4. Change Status")
    print("5. Exit")

    choice = input("\nSelect Option: ")

    if choice == "1":

        issue_key = input(
            "Enter Ticket ID: "
        )

        issue = jira.get_issue(
            issue_key
        )

        print("\n===== TICKET DETAILS =====")

        print(
            f"Key: {issue['key']}"
        )

        print(
            f"Summary: {issue['fields']['summary']}"
        )

        print(
            f"Status: {issue['fields']['status']['name']}"
        )

    elif choice == "2":

        issue_key = input(
            "Enter Ticket ID: "
        )

        issue = jira.get_issue(
            issue_key
        )

        fields = issue["fields"]

        errors = []

        if not fields.get("summary"):
            errors.append(
                "Summary Missing"
            )

        if not fields.get("priority"):
            errors.append(
                "Priority Missing"
            )

        if not fields.get("assignee"):
            errors.append(
                "Assignee Missing"
            )

        if errors:

            print("\nValidation Failed")

            for error in errors:
                print(
                    f" {error}"
                )

        else:

            print(
                "\n Validation Passed"
            )

    elif choice == "3":

        issue_key = input(
            "Enter Ticket ID: "
        )

        print("\nSupported Fields")
        print("1. summary")
        print("2. labels")

        field_map = {
            "1": "summary",
            "2": "labels"
        }

        option = input(
            "\nSelect Option: "
        )

        field_name = field_map.get(
            option
        )

        if not field_name:

            print(
                "Invalid Selection"
            )

            continue

        field_value = input(
            "Enter New Value: "
        )

        if field_name == "labels":

            field_value = [
                label.strip()
                for label in field_value.split(",")
            ]

        jira.update_field(
            issue_key,
            field_name,
            field_value
        )

        print(
            f"\n {field_name} updated"
        )

    elif choice == "4":

        issue_key = input(
            "Enter Ticket ID: "
        )

        transitions = (
            jira.get_transitions(
                issue_key
            )
        )

        print(
            "\nAvailable Transitions"
        )

        for transition in transitions["transitions"]:

            print(
                f"{transition['id']} "
                f"- "
                f"{transition['name']}"
            )

        transition_id = input(
            "\nEnter Transition ID: "
        )

        jira.change_status(
            issue_key,
            transition_id
        )

        print(
            "\n Status Updated"
        )

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print(
            "Invalid Option"
        )