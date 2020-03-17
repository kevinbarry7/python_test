"""
A simple die roller

Author: Kevin Barry
Date: March 16th 2020
"""

import random

first = int(input("Type the first number: "))
last = int(input("Type the last number: "))
print("Choosing a number between "+ str(first) +" and " + str(last)+ ".")
roll = random.randint(int(first),int(last))
print("The number is "+ str(roll)+ '.')
