#!/usr/bin/python3
import sys

argv = sys.argv
argv_sum = 0

for i in range(1, len(argv)):
    argv_sum += int(argv[i])
print("{}".format(argv_sum))
