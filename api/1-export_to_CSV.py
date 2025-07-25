#!/usr/bin/python3
"""Exports employee TODO list to CSV"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Get user info
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get("username")

    # Get user's tasks
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    tasks = todos_response.json()

    # Write to CSV file
    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])
