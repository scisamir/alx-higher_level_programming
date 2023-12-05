#!/usr/bin/python3
"""
Error code #0
"""
from urllib.error import HTTPError
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
