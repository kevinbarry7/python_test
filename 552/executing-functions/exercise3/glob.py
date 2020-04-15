"""  
A module to demonstrate global variables.

Author: Kevin Barry
Date: March 28,2020
"""

# The global variable
VAR = 1

def next():
    """
    Returns and increments the value of VAR.
    """
    global VAR
    result = VAR
    VAR += 1
    return result
