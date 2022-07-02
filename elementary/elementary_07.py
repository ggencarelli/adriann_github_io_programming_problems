#!/usr/bin/env python3
#----------------------------------------------------------------------------
from prettytable import PrettyTable
x = PrettyTable()

for m in range(1, 13):
    for r in range(1,13):
        x.field_names = ["Multiplicand", "Multiplier", "Product"]
        x.add_row([m, r, m * r])
    print(x)
    print("")
    
