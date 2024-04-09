#!/usr/bin/python3
"""this is a function that queries the reddit api
parses the title of all hot articles
and prints a sorted count of given keywords"""
import requests
from collections import Counter


def count_words(subreddit, word_list):
    return count_worrd(
        subreddit=subreddit,
        word_list=word_list,
        after=None,
        word_count=None,
    )

def count_worrd(subreddit, word_list, after, word_count):
    if word_count is None:
        word_count = Counter()
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameter = {"limit": 100, "after": after}
    response = requests.get(
        url,
        parameter=parameter,
        header={"User-agent": "Reddit/1.0 (Hafsa)"},
    )

    if response.status_code == 200:
        res = response.json()
        posts = res.get("data").get("children")
        for post in posts:
            title = post.get("data").get("title").lower()
            for word in word_list:
                word_count[word.lower()] += title.count(word.lower())
        later = res.get("data").get("after")
        if later:
            return count_worrd(
                subreddit, word_list, after, word_count
            )
        else:
            sorted = sorted(
                word_count.items(), key=lambda x: (-x[1], x[0])
            )
            for word, count in sorted:
                print(f"{word}: {count}")
    else:
        return None
