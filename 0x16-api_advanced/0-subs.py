#!/usr/bin/python3
"""Contains a function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    try:
        response = requests.get(
            url, headers={'User-Agent': 'MyPythonScript/1.0'}
            )
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        elif response.status_code == 404:
            return 0
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
