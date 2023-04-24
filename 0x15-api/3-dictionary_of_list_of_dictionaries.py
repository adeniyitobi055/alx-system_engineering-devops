#!/usr/bin/python3
"""
Export data in JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    allTodos = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        allTodos[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(allTodos, f)
