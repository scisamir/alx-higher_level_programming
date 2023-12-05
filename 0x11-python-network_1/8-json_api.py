#!/usr/bin/python3
"""
POST an email #1
"""
import requests
from sys import argv


if __name__ == "__main__":
    q = argv[1] if len(argv) >= 2 else ""

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': q}

    r = requests.post(url, data)

    try:
        r_json = r.json()
        if (r_json == {}):
            print('No result')
        else:
            print(f"[{r_json.get('id')}] {r_json.get('name')}")
    except Exception:
        print('Not a valid JSON')
