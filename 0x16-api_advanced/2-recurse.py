#!/usr/bin/python3
"""
2-recurse module
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """

    global after
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'after': after}
    results = requests.get(url, headers=user_agent, params=params,
                           allow_redirects=False)

    if results.status_code == 200:
        after_data = results.json().get('data').get('after')
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = results.json().get('data').get('children')
        for titles in all_titles:
            hot_list.append(titles.get('data').get('title'))
        return hot_list
    else:
        return (None)
