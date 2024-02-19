#!/usr/bin/python3
"""exporting data from all users,all tasks from all employees"""
import json
import requests
import sys


if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users/"
    todos = "https://jsonplaceholder.typicode.com/todos"
    users = requests.get(user).json()
    # opening a file in write mode
    # info about user is in users
    # info about a users todolist in in todos
    with open("todo_all_employees.json", 'w') as file:
        json.dump({
            user.get("id"): [{
                "username": user.get("username"),
                "task": todo.get("title"),
                "completed": todo.get("completed"),
            } for todo in requests.get(todos,
                                       params={
                                           "userId": user.get("id")}).json()]
            for user in users}, file)
