#!/usr/bin/python3
""" A script that uses a REST API for a given employee ID, returns info
about his/her TODO list progress
"""
import json
import requests
import sys


if __name__ == "__main__":

    employee_id = sys.argv[1]
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    userTodos = requests.get(
        'https://jsonplaceholder.typicode.com/todos',
        params={"userId": employee_id}).json()
    userData = json.loads(user.text)
    with open("{}.json".format(employee_id), "w") as jsonfile:
        json.dump({employee_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": userData["username"]
            } for t in userTodos]}, jsonfile)
