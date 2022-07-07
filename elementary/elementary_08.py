#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
# PROBLEM
#--------------------------------------------------------------------------------------------------
# Write a program that prints all prime numbers. (Note: if your programming language does not
# support arbitrary size numbers, printing all primes up to the largest number you can easily
# represent is fine too.)
#--------------------------------------------------------------------------------------------------

lower = int(input("Please enter the lower number: "))
upper = int(input("Please enter the higher number: "))

for i in range(lower, upper + 1):
    count = 0
    if i > 1:
        for n in range(2, (i//2 + 1)):
            if i % n == 0:
                count = count + 1
                break
    if count == 0:
        print(i)
