#!/usr/bin/python3
"""
Script that fetches employee TODO list progress from a REST API
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays employee TODO list progress from API
    
    Args:
        employee_id (int): The ID of the employee
    """
    base_url = "https://jsonplaceholder.typicode.com"
    
    try:
        # Fetch employee information
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        
        # Fetch employee's todos
        todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        # Extract employee name
        employee_name = user_data.get('name', 'Unknown')
        
        # Calculate task statistics
        total_tasks = len(todos_data)
        completed_tasks = [todo for todo in todos_data if todo.get('completed')]
        num_completed = len(completed_tasks)
        
        # Display results
        print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed, total_tasks))
        
        # Display completed task titles
        for task in completed_tasks:
            title = task.get('title', '')
            print("\t {}".format(title))
            
    except requests.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)
    except (KeyError, ValueError) as e:
        print(f"Error processing data: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>", file=sys.stderr)
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer", file=sys.stderr)
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)