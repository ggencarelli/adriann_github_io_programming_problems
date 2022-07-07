#!/usr/bin/env python3
#--------------------------------------------------------------------------------------------------
# PROBLEM
#--------------------------------------------------------------------------------------------------
# Write a program that prints the next 20 leap years.
#--------------------------------------------------------------------------------------------------

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = int(date.strftime("%Y"))

year_list = []

while len(year_list) <= 20:
    if year % 4 == 0:
        year_list.append(year)
        year = year + 1
    else:
        print(year, "is not a leap year!")
        year = year + 1

print(" ")
for i in year_list:
    print(i, "is a leap year!")

