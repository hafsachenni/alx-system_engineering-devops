#!/usr/bin/python3
"""returning info about someones todolist usinf rest api"""
import json
import requests
import sys


if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users/"
    todos = "https://jsonplaceholder.typicode.com/todos"
    response_user = requests.get(user + "{}".format(sys.argv[1])).json()
    response_todo = requests.get(todos, params={"userId": sys.argv[1]}).json()

    id = sys.argv[1]
    name = response_user.get("username")
    json_file = "{}.json".format(id)

    with open(json_file, "w") as file:
        json.dump({id: [{
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": name
        } for task in response_todo]}, file)
