#!/usr/bin/env python3
#----------------------------------------------------------------------------
# PROBLEM
# Write function that reverses a list, preferably in place. 
#----------------------------------------------------------------------------

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
    my_list.reverse()
    print("My reversed list is:")
    for i in my_list:
        print(i)

if __name__ == "__main__":
    main()
