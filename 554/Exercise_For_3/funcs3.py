"""
Module with range-based for-loop functions.

Author: Kevin Barry
Date: May 23, 2020
"""


def factorial(n):
    """
    Returns n! = n * (n-1) * (n-2) ... * 1

    0! is 1.  Factorial is undefined for integers < 0.

    Examples:
        factorial(0) returns 1
        factorial(2) returns 2
        factorial(3) returns 6
        factorial(5) returns 120

    Parameter n: The integer for the factorial
    Precondition: n is an int >= 0
    """
    assert type(n) == int
    assert n >= 0

    result = 1
    for i in range(n, 0, -1):
        result = result * i
    return result


def revrange(a, b):
    """
    Returns the tuple (b-1, b-2, ..., a)

    Note that this tuple is the reverse of tuple(range(a,b))

    Parameter a: the "start" of the range
    Precondition: a is an int <= b

    Parameter b: the "end" of the range
    Precondition: b is an int >= a
    """

    assert (type(a) == int) and (type(a) == int)
    assert a <= b

    z = ()
    y = ()
    for i in range(a, b):
        z = z + (i,)
    print(z)
    for i in z[::-1]:
        y = y + (i,)
    print(y)





print(factorial(0))  # returns 1
print(factorial(2))  # returns 2
print(factorial(3))  # returns 6
print(factorial(5))  # returns 120
print()
revrange(2, 6)
# revrange(0, 3)