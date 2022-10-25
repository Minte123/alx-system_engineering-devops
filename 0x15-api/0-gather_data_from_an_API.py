#!/usr/bin/python3
"""
API CALL
"""
import requests
import sys


if __name__ == "__main__":
    try:
        userId = int(sys.argv[1])
    except (IndexError, TypeError, ValueError):
        sys.exit(0)
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(
        str(userId))).json()
    completed = 0
    totals = 0
    tasks_complted = []
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    for task in tasks:
        if task.get("userId") == int(sys.argv[1]) and task.get("completed"):
            completed += 1
            tasks_complted.append(task.get("title"))
        if task.get("userId") == int(sys.argv[1]):
            totals += 1
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), completed, totals))
    for t in tasks_complted:
        print("\t {}".format(t))
