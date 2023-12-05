#!/usr/bin/python3
"""
My GitHub!
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    usrn = argv[1]
    pswd = argv[2]

    r = requests.get(
            'https://api.github.com/user',
            auth=HTTPBasicAuth(usrn, pswd)
        )

    print(r.json().get('id'))
