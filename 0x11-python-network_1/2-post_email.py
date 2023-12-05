#!/usr/bin/python3
"""
POST an email #0
"""
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from sys import argv


if __name__ == "__main__":
    url = argv[1]

    email = urlencode({'email': argv[2]})
    email = email.encode('ascii')

    req = Request(url, email)

    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
