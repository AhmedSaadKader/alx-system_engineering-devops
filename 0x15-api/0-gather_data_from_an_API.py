#!/usr/bin/python3
""" A script that uses a REST API for a given employee ID, returns info
about his/her TODO list progress
"""
import requests
import sys
import json


if __name__ == "__main__":
    completed = []
    employee_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id))
    userTodos = requests.get('https://jsonplaceholder.typicode.com/todos', params={"userId": employee_id}).json()
    userData = json.loads(user.text)
    for item in userTodos:
        if item.get("completed") is True:
            completed.append(item.get("title"))
    print('Employee {} is done with tasks({}/{}):'.format(userData["name"], len(completed), len(userTodos) ))
    for task in completed:
        print('\t {}'.format(task))
