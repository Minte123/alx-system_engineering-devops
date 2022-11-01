#!/usr/bin/python3

"""
Get title of top ten hot posts
"""
import requests


def top_ten(subreddit):
    """ Get title of top ten posts in each subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Minte-net"}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code == 200:
        top = resp.json().get("data").get("children")[:10]
        for sub in top:
            print(sub.get("data").get("title"))
    else:
        print("None")
