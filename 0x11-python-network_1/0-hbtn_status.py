#!/usr/bin/python3
"""
fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as response:
        res = response.read()
        print(f"Body response:\n\t- type: {type(res)}\n\t- content: {res}\
\n\t- utf8 content: {res.decode('utf-8')}")
