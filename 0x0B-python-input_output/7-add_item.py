#!/usr/bin/python3
""" Load, add, save """

from sys import argv
from os import path
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


def add_item():
    json_load = []

    if path.exists("add_item.json"):
        json_load = load_from_json_file("add_item.json")
        json_load += argv[1:]
    else:
        with open("add_item.json", 'w', encoding="utf-8") as f:
            json_load = argv[1:]
            f.write("")

    save_to_json_file(json_load, "add_item.json")


if __name__ == "__main__":
    add_item()
