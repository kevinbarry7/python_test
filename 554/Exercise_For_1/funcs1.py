"""
Module with simple for-loop functions.

Author: Kevin Barry
Date: May 21, 2020
"""


def lesser(tup, value):
    """
    Returns the number of elements in tup strictly less than value

    Examples:
        lesser((5, 9, 1, 7), 6) returns 2
        lesser((1, 2, 3), -1) returns 0

    Parameter tup: the tuple to check
    Precondition: tup is a non-empty tuple of ints

    Parameter value:  the value to compare to the tuple
    Precondition:  value is an int
    """
    assert len(tup) != 0

    acc_value = 0
    for x in tup:
        if x < value:
            acc_value += 1
    return acc_value


def avg(tup):
    """
    Returns average of all of the elements in the tuple.

    Remember that the average of a tuple is the sum of all of the elements in the
    tuple divided by the number of elements in the tuple.

    Examples:
        avg((1.0, 2.0, 3.0)) returns 2.0
        avg((1.0, 1.0, 3.0, 5.0)) returns 2.5

    Parameter tup: the tuple to check
    Precondition: tup is a tuple of numbers (int or float)
    """
    total = 0
    count = 0

    for num in tup:
        total += num
        count += 1
    if total == 0 or count == 0:
        return 0
    else:
        avg = total/count
        return avg


result = avg(())
print(result)

result = avg((7, 1, 4, 3, 6, 8))
print(result)

result = avg((-1, 1, 3, 5))
print(result)

result = avg((2.5,))
print(result)



result = avg((1.0, 1.0, 1.0))
print(result)
# introcs.assert_floats_equal(1.0, result)
#
# tup = tuple(range(10, 20))
# result = funcs.avg(tup)
# introcs.assert_floats_equal(14.5, result)
