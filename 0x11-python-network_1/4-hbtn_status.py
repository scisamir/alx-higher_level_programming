#!/usr/bin/python3
"""
What's my status? #1
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:\n\t- type: {type(r.text)}\n\t- content: {r.text}")
