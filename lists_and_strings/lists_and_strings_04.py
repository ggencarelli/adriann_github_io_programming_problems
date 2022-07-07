#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
# PROBLEM
#--------------------------------------------------------------------------------------------------
# Write a function that returns the elements on odd positions in a list. 
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
    my_list = build_list()
    for i in my_list:
        my_index = my_list.index(i)
        if my_index % 2 != 0:
            print(i, "occurs at an odd position!")

if __name__ == "__main__":
    main()
