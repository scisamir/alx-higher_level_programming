#!/usr/bin/python3
"""
Response header value #1
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])

    print(r.headers['X-Request-Id'])
