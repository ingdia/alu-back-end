#!/usr/bin/python3
"""
Access employee TODO list progress from a REST API
"""

import requests
from sys import argv


def get_employee_todos_progress(employee_id):
    """Fetch and display TODO list progress for an employee"""
    try:
        url = "https://jsonplaceholder.typicode.com"

        # Get employee info
        user_response = requests.get(f"{url}/users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data['name']

        # Get todos
        todos_response = requests.get(f"{url}/todos?userId={employee_id}")
        todos = todos_response.json()

        total_tasks = len(todos)
        done_tasks = [task for task in todos if task['completed']]
        done_count = len(done_tasks)

        # Print progress
        print(f"Employee {employee_name} is done with tasks ({done_count}/{total_tasks}):")

        # Print completed task titles
        for task in done_tasks:
            print(f"\t {task['title']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        get_employee_todos_progress(argv[1])
