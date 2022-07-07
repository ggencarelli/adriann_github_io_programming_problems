#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
# PROBLEM
#--------------------------------------------------------------------------------------------------
# Modify the previous program such that only multiples of three or five are considered in the sum, 
# e.g. 3, 5, 6, 9, 10, 12, 15 for n=17
#--------------------------------------------------------------------------------------------------

num = int(input("Please enter a number: "))
catch = []
for i in range(1, num):
    if i % 3 == 0 or i % 5 == 0:
        catch.append(i)
total = sum(catch)
print(total)    
