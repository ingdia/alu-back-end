#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

This script retrieves and displays the TODO list progress for a given employee
from a REST API. It takes an employee ID as a command-line argument and fetches
the employee's name, the number of completed tasks, and the total number of tasks.
The results are printed in a specified format.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Arguments:
    <employee_id> : An integer representing the ID of the employee.

Example:
    python3 0-gather_data_from_an_API.py 2
"""

import requests
import sys

def main(employee_id):
    # Define the API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    
    # Fetch TODO data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data.get('name', 'Unknown')

    # Calculate completed and total tasks
    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Display the results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        main(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
