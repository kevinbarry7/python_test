"""
A simple die roller

Author: Kevin Barry
Date: March 16th 2020
"""

import random
first = 1
last = 6
roll = random.randint(first,last)
print("Choosing a number between "+ str(first) +" and " + str(last)+ ".")
print("The number is "+ str(roll)+ '.')
