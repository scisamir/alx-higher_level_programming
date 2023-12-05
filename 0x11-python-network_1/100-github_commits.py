#!/usr/bin/python3
"""
Time for an interview!
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    r = requests.get(url)

    r_json = r.json()

    i = 0
    for item in r_json:
        if i > 9:
            break
        print(f"{item.get('sha')}: \
{item.get('commit').get('author').get('name')}")
        i += 1
