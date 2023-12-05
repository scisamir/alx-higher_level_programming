#!/usr/bin/python3
"""
My GitHub!
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(
            'https://api.github.com/user',
            auth=('scisamir', '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')
        )

    print(r.json().get('id'))
