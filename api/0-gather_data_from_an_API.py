#!/usr/bin/python3
"""
Access employee TODO list progress from a REST API
"""

import requests
from sys import argv
""" modules to work with """ 

def get_employee_todos_progress(employee_id):
    """  a function to get employee info about Todo list"""
    try:
        url =   "https://jsonplaceholder.typicode.com"
        # user_info = requests.get(f"{url}/users/{employee_id}")
        user_datas = requests.get(url + f"/users/{employee_id}")
        user_data = user_datas.json()
        employee_name = user_data['name']

        """fetching the todos of the employee"""
        todos_list = requests.get(url +f"/todos?userId={employee_id}")
        json_todos_list = todos_list.json()

        total_tasks = len(json_todos_list)
        task_done = [task for task in json_todos_list if task['completed']]  
        no_task_done = len(task_done)

        """returning the employee info and tasks done"""
        print(f"Employee {employee_name} is done with task("
              f"{no_task_done}/{total_tasks}):")
        
        """title of completed tasks"""
        for task in task_done:
            print(f"\t {task['title']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    if len(argv) != 2:
         print("Usage: Script <employee_id>")
    else:
        get_employee_todos_progress(argv[1]) 


          

  