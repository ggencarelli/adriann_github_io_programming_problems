#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
# PROBLEM
#--------------------------------------------------------------------------------------------------
# Write a function that checks whether an element occurs in a list.
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
    my_num = int(input("Enter a number between 1 and 1000: "))
    match = False
    for i in my_list:
        if i == my_num:
            match = True
            print(i, "is in the list!")
    if match == False:
        print(my_num, "is not in the list!")

if __name__ == "__main__":
    main()
