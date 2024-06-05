#!/usr/bin/python3
"""Contains top_ten function that queries the Reddit API and prints
the title of the first 10 hot posts listed
"""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed
    for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyPythonScript/1.0'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        posts = data.get("data", {}).get("children", [])

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except requests.exceptions.RequestException:
        print("None")
