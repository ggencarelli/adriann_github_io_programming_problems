#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
# PROBLEM
#--------------------------------------------------------------------------------------------------
# Write a function that computes the running total of a list. 
#--------------------------------------------------------------------------------------------------

import random

total = 0

def build_list():
    num_list = [17, 34, 764, 12, 32, 9]
    total = 0
    for i in num_list:
        total = total + i
        print("The total is", total)

def main():
    build_list()

if __name__ == "__main__":
    main()
