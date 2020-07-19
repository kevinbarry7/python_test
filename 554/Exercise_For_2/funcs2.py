"""
Module with more complex for-loop functions.

All of these functions make use of accumulators that make new tuples.

Author: Kevin Barry
Date: May 22, 2020
"""


def clamp(tup, min, max):
    """
    Returns a copy of tup where every element is between min and max.

    Any number in the tuple less than min is replaced with min.  Any number
    in the tuple greater than max is replaced with max. Any number between
    min and max is left unchanged.

    Examples:
        clamp((-1, 1, 3, 5),0,4) returns (0,1,3,4)
        clamp((-1, 1, 3, 5),-2,8) returns (-1,1,3,-5)
        clamp((-1, 1, 3, 5),-2,-1) returns (-1,-1,-1,-1)
        clamp((),0,4) returns ()

    Parameter tup: the tuple to copy
    Precondition: tup is a tuple of numbers (float or int)

    Parameter min: the minimum value for the tuple
    Precondition: min <= max is a number

    Parameter max: the maximum value for the tuple
    Precondition: max >= min is a number
    """
    assert min <= max
    assert max >= min
    y = ()
    for x in tup:
        if x < min:
            x = min
            y = y + (x,)
        elif x > max:
            x = max
            y = y + (x,)
        else:
            y = y + (x,)
    print(y)


def uniques(tup):
    """
    Returns the number of unique elements in the tuple.

    Examples:
        uniques((5, 9, 5, 7)) returns 3
        uniques((5, 5, 1, 'a', 5, 'a')) returns 3
        uniques(()) returns 0

    Parameter tup: the tuple to copy
    Precondition: tup is a tuple
    """
    unique = ()
    for x in tup:
        if x not in unique:
            unique = unique + (x,)
    print(unique)


clamp((-1, 1, 3, 5), 0, 4)
clamp((-1, 1, 3, 5), -2, 8)
clamp((-1, 1, 3, 5), -2, -1)
clamp((-1, 1, 3, 5), 1, 1)
clamp((1, 3), 0, 4)
clamp((), 0, 4)

uniques((5, 9, 5, 7))
uniques((5, 5, 1, 'a', 5, 'a'))
uniques((1, 2, 3, 4, 5))
uniques((1,))
uniques(())