#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)

    for name in range(len(names)):
        if names[name][0] == '_' and names[name][1] == '_':
            continue
        print("{}".format(names[name]))
