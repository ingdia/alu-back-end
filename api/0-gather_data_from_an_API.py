#!/usr/bin/python3
"""
Access employee TODO list progress from a REST API
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    employee_name = user.get("name")

    # Get todos
    todos = requests.get(f"{base_url}/todos", params={"userId": employee_id}).json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]

    # Output
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
