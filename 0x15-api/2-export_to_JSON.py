#!/usr/bin/python3
"""
API CALL
"""
import json
import requests
import sys


if __name__ == "__main__":
    try:
        userId = int(sys.argv[1])
    except (IndexError, TypeError, ValueError):
        sys.exit(0)
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(
            str(userId))).json()
    username = user.get("username")
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos/?userId={}".format(
            userId)).json()
    with open("{}.json".format(userId), "w", encoding="utf-8") as f:
        json.dump({str(userId): [{"task": task.get("title"),
                                  "completed": task.get("completed"),
                                  "username": username}
                                 for task in tasks]}, f)
