#!/usr/bin/python3

"""
Get subscribers count of a subreddit
"""
import requests


def number_of_subscribers(subreddit: str):
    """ Get number_of_subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Access-Redt-API/v.0.1"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        result = response.json().get("data")
        subs = result.get("subscribers")
        return subs
    return 0
