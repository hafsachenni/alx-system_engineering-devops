#!/usr/bin/python3
"""fetching data from an api in csv format"""
import csv
import requests
import sys


if __name__ == "__main__":
    user = "https://jsonplaceholder.typicode.com/users/"
    todos = "https://jsonplaceholder.typicode.com/todos"
    response_user = requests.get(user + "{}".format(sys.argv[1])).json()
    response_todo = requests.get(todos, params={"userId": sys.argv[1]}).json()

    id = sys.argv[1]
    name = response_user.get("username")

    """creation of csv file to write data into it + quote everything"""
    csv_file = "{}.csv".format(id)
    with open(csv_file, mode='w') as file:
        csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        """writing DATA for each task"""
        for task in response_todo:
            task_completed_status = (
                "True" if task.get("completed") else "False"
            )
            csv_writer.writerow([
                id,
                name,
                task_completed_status,
                task.get("title")
            ])
