#!/usr/bin/env python3
#----------------------------------------------------------------------------
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
