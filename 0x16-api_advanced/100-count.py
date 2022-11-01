#!/usr/bin/python3
'''
displays top 10 hot posts
'''
import requests


def count_words(subreddit, word_list, after=None, result=[]):
    user_agent = {'User-agent': 'greg'}
    sub = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                       .format(subreddit, after), headers=user_agent)

    sub = sub.json().get('data')
    after = sub.get('after')
    sub = sub.get('children')
    for obj in sub:
        title = obj['data'].get('title').split(' ')
        for words in title:
            word = words.lower()
            if word in word_list:
                result.append(word)
    if after is not None:
        count_words(subreddit, word_list, after, result)
    else:
        dict_res = {}
        for word in word_list:
            dict_res[word] = 0
        for i in result:
            dict_res[i] += 1
        for v in sorted(dict_res.values(), reverse=True):

            for k in dict_res:
                if dict_res[k] == v and v != 0:
                    print("{}: {}".format(k, v))
