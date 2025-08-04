#!/usr/bin/python3
"""
Exports employee TODO list to a JSON file.
"""

import json
import requests
from sys import argv


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        exit(1)

    try:
        employee_id = int(argv[1])
        url = "https://jsonplaceholder.typicode.com"

        # Fetch user data
        user_url = f"{url}/users/{employee_id}"
        user_res = requests.get(user_url)
        user_res.raise_for_status()
        user = user_res.json()
        username = user.get("username")

        # Fetch todos
        todos_url = f"{url}/todos?userId={employee_id}"
        todos_res = requests.get(todos_url)
        todos_res.raise_for_status()
        todos = todos_res.json()

        # Build JSON structure
        tasks = [{
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        } for task in todos]

        data = {str(employee_id): tasks}

        # Write to JSON file
        filename = f"{employee_id}.json"
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f)

    except ValueError:
        print("Employee ID must be an integer.")
    except requests.RequestException as err:
        print(f"Network error: {err}")
    except Exception as err:
        print(f"An error occurred: {err}")
