#!/usr/bin/python3
"""
API CALL
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    with open("todo_all_employees.json", "w", encoding="utf-8") as f:
        total = {}
        for user in users:
            userId = user.get("id")
            username = user.get("username")
            u = []
            for task in tasks:
                if task.get("userId") == userId:
                    u.append({"task": task.get("title"),
                              "completed": task.get("completed"),
                              "username": username})
            total[userId] = u
        json.dump(total, f)
