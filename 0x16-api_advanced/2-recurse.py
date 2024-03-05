#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed for a given subreddit"""

import requests

def recurse(subreddit, hot_list=[]):
    """function that queries the Reddit API and prints titles of hot posts"""
    if subreddit is None:
        print(None)
    if after:
        url += f'&after={after}'
    url = 'http://www.reddit.com/r/{}/hot.json'.format(subreddit)
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        """now lets check if children key is present in the response"""
        if 'children' in data['data']:
            for post in data['data']['children']:
                hot_list.append(post['data']['title'])

            """checking if we have paginated data that we have to go through"""
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                """return the final hot list if there is no pages left"""
                return hot_list
        else:
            """return none if children was not found in response"""
            return None
    else:
        """none, if request was unsuccessful"""
        return None
