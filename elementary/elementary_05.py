#!/usr/bin/env python3
#----------------------------------------------------------------------------
num = int(input("Please enter a number: "))
catch = []
for i in range(1, num):
    if i % 3 == 0 or i % 5 == 0:
        catch.append(i)
total = sum(catch)
print(total)    
