#!/usr/bin/python3
"""
Export data in JSON format
"""
import json
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(userId))
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    userTodo = {}
    taskList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": user.json().get("username")}
            taskList.append(taskDict)
    userTodo[userId] = taskList

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(userTodo, f)
