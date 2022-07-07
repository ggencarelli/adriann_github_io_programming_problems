#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
# PROBLEM
#--------------------------------------------------------------------------------------------------
# Write a function that returns the largest element in a list.
#--------------------------------------------------------------------------------------------------

import random

def build_list():
    num_list = []
    while True:
        rand = random.randint(1, 1000)
        num_list.append(rand)
        if len(num_list) > 50:
            break
    return num_list

def main():
    high = max(build_list())
    print("The highest number in my list is", high)

if __name__ == "__main__":
    main()
