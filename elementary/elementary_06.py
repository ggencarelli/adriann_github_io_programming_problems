#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
# PROBLEM
#--------------------------------------------------------------------------------------------------
# Write a program that asks the user for a number n and gives them the possibility to choose between
# computing the sum and computing the product of 1,…,n.
#--------------------------------------------------------------------------------------------------

num = int(input("Please enter a number: "))
choice = input("Would you like the sum or the product of the range? ")
if choice == "sum":
    print(sum(range(1, num)))
else:
    result = 1
    for i in range(1, num):
        result = i * result
    print(result)
