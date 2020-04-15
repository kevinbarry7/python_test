"""
A module to show off what happens when an error occurs

Author: Walker M. White
Date:   March 1, 2019
"""


def function_1(x,y):
    """
    Returns: result of function_2
    
    Precondition: x is a number
    Precondition: y is a number
    """
    return function_2(x,y)


def function_2(x,y):
    """
    Returns: result of function_3
    
    Precondition: x is a number
    Precondition: y is a number
    """
    return function_3(x,y)


def function_3(x,y):
    """
    Returns: x divided by y
    
    Precondition: x is a number
    Precondition: y is a number, y > 0
    """
    return x/y


# Script Code
print(function_1(2,3))
print(function_1(1,0))
