#!/usr/bin/python3

"""
Get title of top ten hot posts
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Recursively get data """
    url = "https://www.reddit.com/r/{}/hot.json?limit=100&after={}".format(
        subreddit, after)
    headers = {"User-Agent": "Getacher-Top-Ten"}
    resp = requests.get(url, headers=headers, allow_redirects=False)
    if resp.status_code != 200:
        return None
    after = resp.json().get("data").get("after")
    ch = resp.json().get("data").get("children")
    for item in ch:
        hot_list.append(item.get("data").get("title"))
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
