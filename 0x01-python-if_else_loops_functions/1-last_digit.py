#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
print("Last digit of {} is ".format(number), end='')
if number < 0:
    last_digit *= -1
if last_digit == 0:
    print("{} and is 0".format(last_digit))
elif last_digit < 6 and last_digit != 0:
    print("{} and is less than 6 and not 0".format(last_digit))
elif last_digit > 5:
    print("{} and is greater than 5".format(last_digit))
