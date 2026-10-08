from jira_client import JiraClient

jira = JiraClient()

issue_key = input(
    "Enter Jira Ticket ID: "
)

transitions = jira.get_transitions(
    issue_key
)

print("\nAvailable Status Changes:")

for transition in transitions["transitions"]:

    print(
        f"ID: {transition['id']} "
        f"-> {transition['name']}"
    )

transition_id = input(
    "\nEnter Transition ID: "
)

jira.change_status(
    issue_key,
    transition_id
)

print(
    f"\n✅ Status updated successfully "
    f"for {issue_key}"
)