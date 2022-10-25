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
    with open("{}.csv".format(userId), "w", encoding="utf-8") as f:
        for task in tasks:
            if task.get("userId") == int(sys.argv[1]):
                f.write('"{}","{}","{}","{}"\n'.format(
                    userId, user.get("username"),
                    task.get("completed"),
                    task.get("title")))
