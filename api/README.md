# ALU Back-End - API Project

## Project Overview

This project demonstrates how to interact with a REST API to retrieve employee data and their TODO list progress. It is designed as part of the African Leadership University (ALU) backend curriculum, showcasing the use of Python to work with APIs instead of traditional shell scripting.

## Script: 0-gather_data_from_an_API.py

This Python script fetches an employee’s TODO list from a public REST API and displays their progress in completing tasks.

### Features

- Accepts an employee ID as a command-line argument.
- Fetches employee information (name).
- Fetches the TODO list of that employee.
- Displays the number of completed tasks out of the total.
- Lists the titles of completed tasks in a formatted output.

### Requirements

- Python 3.4 or higher
- `requests` Python module

### Installation

Make sure you have Python 3 installed. To install the `requests` module, run:

```bash
pip install requests
