#!/usr/bin/python3
import requests
import sys

def main(employee_id):
    # Define the API URLs
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user data
    user_response = requests.get(user_url)
    user_data = user_response.json()
    
    # Fetch TODOs data
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Extract employee name
    employee_name = user_data.get('name')

    # Calculate completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = [todo['title'] for todo in todos_data if todo['completed']]
    number_of_done_tasks = len(completed_tasks)

    # Display the results
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
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
