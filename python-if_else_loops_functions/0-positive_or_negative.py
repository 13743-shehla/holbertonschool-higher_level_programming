#!/usr/bin/python3
from random import randint

number = randint(-100, 100)

if number > 0:
    print(str(number) + " is positive")
elif number == 0:
    print(str(number) + " is zero")
else:
    print(str(number) + " is negative")
