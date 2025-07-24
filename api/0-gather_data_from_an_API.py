#!/usr/bin/python3
"""Access employee TODO list progress from a REST API"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = user.get("name")

    # Get todos for employee
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()
    done_tasks = [task for task in todos if task.get("completed")]

    # Print the summary line exactly as required
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), len(todos)))

    # Print completed task titles, formatted with a tab
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
