#!/usr/bin/python3
""" A script that uses a REST API for a given employee ID, returns info
about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user.get("username")
            } for task in requests.get("https://jsonplaceholder.typicode.com/todos",
                                    params={"userId": user.get("id")}).json()]
            for user in users}, jsonfile)
