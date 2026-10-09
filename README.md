# Jira CRUD Automation Platform

## Project Overview

The Jira CRUD Automation Platform is a DevOps automation solution built using **Python**, **Jira REST APIs**, and **GitHub Actions**.

The project enables users to perform Jira ticket operations directly from GitHub Actions by providing workflow inputs such as Ticket ID, Operation Type, Field Name, and Field Value.

The solution eliminates manual Jira activities and provides a self-service interface for interacting with Jira tickets through automated workflows.

---

## Technologies Used

- Python
- Jira REST API
- GitHub Actions
- Requests Library
- Python Dotenv
- GitHub Secrets

---

## Key Features

### Create

Create a new Jira sub-task under an existing parent ticket.

Example:

```text
Parent Ticket: SYSINT-15258

Sub-task Summary:
Validate GitHub Action Outputs
```

Output:

```text
SYSINT-15300 Created Successfully
```

---

### Read

Retrieve ticket information dynamically using a user-provided Jira ticket ID.

Information retrieved includes:

- Ticket Key
- Summary
- Status
- Priority
- Assignee
- Labels

Example:

```text
SYSINT-15258
```

Output:

```text
Summary: Jira CRUD Demo
Status: To Do
Priority: Medium
Assignee: Sandeep Kancharla
```

---

### Update

Update editable Jira fields through workflow inputs.

Supported fields include:

- Summary
- Description
- Labels
- Priority
- Due Date
- Components
- Fix Versions

Workflow first discovers editable fields from Jira metadata and then allows the user to update the selected field.

---

### Status Transition

Move Jira tickets through the workflow lifecycle.

Examples:

```text
To Do
↓
In Progress
↓
Done
```

The application retrieves valid transitions directly from Jira and only allows supported workflow transitions.

---

### Validation

Validate Jira tickets before performing actions.

Validation checks include:

- Summary Exists
- Status Exists
- Priority Exists
- Assignee Exists

Example Output:

```text
Validation Passed
```

or

```text
Validation Failed

Priority Missing
Assignee Missing
```

---

### Get Editable Fields

Retrieve all editable fields and metadata from Jira.

Example Output:

```text
summary        | Summary        | string
description    | Description    | rich text
priority       | Priority       | option
labels         | Labels         | array
duedate        | Due Date       | date
components     | Components     | array
fixVersions    | Fix Versions   | array
```

This feature allows the Update operation to be dynamic and reusable across different Jira tickets.

---

# Project Architecture

```text
+------------------------------------------------+
|                 GitHub Actions                 |
+------------------------------------------------+
                    |
                    |
                    v

+------------------------------------------------+
|              Workflow User Inputs              |
+------------------------------------------------+
| Ticket ID                                      |
| Operation                                      |
| Field Name                                     |
| Field Value                                    |
+------------------------------------------------+
                    |
                    |
                    v

+------------------------------------------------+
|                jira_runner.py                  |
+------------------------------------------------+
| Read                                            |
| Validate                                        |
| Get Editable Fields                             |
| Update Fields                                   |
| Create Subtasks                                 |
| Change Status                                   |
+------------------------------------------------+
                    |
                    |
                    v

+------------------------------------------------+
|                jira_client.py                  |
+------------------------------------------------+
| Jira Authentication                             |
| Jira REST API Communication                     |
| Error Handling                                  |
| Payload Construction                            |
+------------------------------------------------+
                    |
                    |
                    v

+------------------------------------------------+
|                 Jira REST APIs                 |
+------------------------------------------------+
| GET Issue                                      |
| GET Edit Metadata                              |
| GET Transitions                                |
| PUT Update Issue                               |
| POST Create Sub-task                           |
| POST Transition Issue                          |
+------------------------------------------------+
                    |
                    |
                    v

+------------------------------------------------+
|                  Jira Project                  |
+------------------------------------------------+
| Parent Tickets                                 |
| Sub-tasks                                      |
| Status Changes                                 |
| Field Updates                                  |
+------------------------------------------------+
```

---

# Flow of Control

## Read Ticket

```text
GitHub Actions
      ↓
User Enters Ticket ID
      ↓
jira_runner.py
      ↓
jira_client.py
      ↓
GET Jira Issue
      ↓
Display Ticket Details
```

---

## Validate Ticket

```text
GitHub Actions
      ↓
User Enters Ticket ID
      ↓
Retrieve Ticket
      ↓
Validate Required Fields
      ↓
Display Validation Results
```

---

## Get Editable Fields

```text
GitHub Actions
      ↓
User Enters Ticket ID
      ↓
Retrieve Edit Metadata
      ↓
Display Editable Fields
      ↓
Display Field Types
```

---

## Update Field

```text
GitHub Actions
      ↓
Ticket ID
Field Name
Field Value
      ↓
Validate Editable Field
      ↓
Build REST API Payload
      ↓
Update Jira Issue
      ↓
Verify Updated Values
```

---

## Create Sub-task

```text
GitHub Actions
      ↓
Parent Ticket ID
Sub-task Summary
      ↓
Create Jira Sub-task
      ↓
Return New Issue Key
```

---

## Status Transition

```text
GitHub Actions
      ↓
Ticket ID
Target Status
      ↓
Retrieve Available Transitions
      ↓
Validate Transition
      ↓
Execute Transition
      ↓
Verify New Status
```

---

# Security Design

Sensitive information is stored using GitHub Secrets.

```text
JIRA_BASE_URL
JIRA_EMAIL
JIRA_API_TOKEN
```

Credentials are never stored in source code.

---

# Benefits

- Reduces manual Jira operations
- Enables self-service Jira management
- Standardizes ticket updates
- Supports enterprise DevOps workflows
- Demonstrates Python API integration
- Demonstrates CI/CD automation using GitHub Actions
- Reusable across multiple Jira projects and tickets

---

# Summary

This project demonstrates how Python, Jira REST APIs, and GitHub Actions can be combined to create a self-service DevOps automation platform capable of:

- Creating Jira Sub-tasks
- Reading Jira Tickets
- Updating Editable Jira Fields
- Validating Jira Tickets
- Discovering Editable Fields
- Performing Workflow Status Transitions

The solution provides a scalable and reusable framework for Jira automation within enterprise CI/CD environments.
