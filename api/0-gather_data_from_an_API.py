#!/usr/bin/python3
"""
Access employee TODO list progress from a REST API
"""

import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user_response = requests.get(f"{base_url}/users/{emp_id}")
    user = user_response.json()
    employee_name = user.get("name")

    # Get employee's todos
    todos_response = requests.get(f"{base_url}/todos", params={"userId": emp_id})
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Print header
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    # Print completed tasks
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
