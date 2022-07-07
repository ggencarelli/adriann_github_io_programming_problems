#!/usr/bin/env python3
#----------------------------------------------------------------------------
import random

rand = random.randint(1, 100)

while True:
    num = int(input("Please guess a number between 1 and 100: "))
    if num == rand:
        print("That's correct!")
        break
    elif num > rand:
        print("Lower. Try again.")
        continue
    else:
        print("Higher. Try again.")
