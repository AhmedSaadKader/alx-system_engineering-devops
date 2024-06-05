#!/usr/bin/python3
"""Contains the function recurse which is a recursive function that queries
the reddit api and returns a list containing the titles of all hot
articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches hot article titles for a subreddit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyPythonScript/1.0'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get("data", {}).get("children", [])
            for post in posts:
                hot_list.append(post.get("data", {}).get("title"))

            after = data.get("data", {}).get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        elif response.status_code == 404:
            return None
        else:
            return hot_list
    except requests.exceptions.RequestException:
        return None
