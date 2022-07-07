#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
# PROBLEM
#--------------------------------------------------------------------------------------------------
# Write a guessing game where the user has to guess a secret number. After every guess the program
# tells the user whether their number was too large or too small. At the end the number of tries
# needed should be printed. It counts only as one try if they input the same number multiple times
# consecutively.
#--------------------------------------------------------------------------------------------------

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
