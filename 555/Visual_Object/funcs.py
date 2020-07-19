"""
Functions demonstrating using other functions as parameters.

These two functions are implementations of the famous fold functions.  A variation of
fold is called "reduce", which is part of Google's famous map-reduce set-up.

Author: Kevin Barry
Date: May 30, 2020
"""


def sub(x, y):
    """
    Returns the difference x-y

    Parameter x: The value to subtract from
    Precondition: x is a number

    Parameter y: The value to subtract
    Precondition: y is a number
    """
    return x - y


def remove(s1, s2):
    """
    Returns a copy of s, with all characters in s2 removed.

    Examples:
        remove('abc','ab') returns 'c'
        remove('abc','xy') returns 'abc'
        remove('hello world','ol') returns 'he wrd'

    Parameter s1: the string to copy
    Precondition: s1 is a string

    Parameter s2: the characters to remove
    Precondition: s2 is a string
    """
    result = ''
    for x in s1:
        if not x in s2:
            result = result + x
    return result


def add(x, y):
    """
    Returns the sum x+y

    This works on any types that support addition (numbers, strings, etc.)

    Parameter x: The first value to add
    Precondition: x supports addition and x is same type as y

    Parameter x: The second value to add
    Precondition: x supports addition and x is same type as y
    """
    return x + y


def fold_left(f, seq, value):
    """
    Returns the result of folding f left over seq, starting with value.

    To fold a function f from the left, we
    * Start with value in the accumulator
    * Iterate over the sequence normally
    * At each step, apply f to the accumulator and the next element
    * After applying f, make the new value the accumulator

    Example: Suppose f is - (subtraction), seq is (1,2,3,4) and value is 0.  Then
    the result is

        ((((0-1)-2)-3)-4) = -10

    Parameter f: the function to fold
    Precondition: f is a function that takes two arguments of the same time, and
    returning a value of the same type

    Parameter seq: the sequence to fold
    Precondition: seq is a sequence (tuple, string, etc.) whose elements are the
    same type as that returned by f

    Parameter value: the initial starting value
    Precondition: value has the same type as the return type of f
    """
    accum = value
    for x in seq:
        accum = f(accum, x)
    return accum


def fold_right(f, seq, value):
    """
    Returns the result of folding f right over seq, starting with value.

    To fold a function f from the right, we
    * Start with value in the accumulator
    * Iterate over the sequence right-to-left
    * At each step, apply f to the next element and the accumulator
    * After applying f, make the new value the accumulator

    Example: Suppose f is - (subtraction), seq is (1,2,3,4) and value is 0.  Then
    the result is

        (1-(2-(3-(4-0)))) = -2

    Parameter f: the function to fold
    Precondition: f is a function that takes two arguments of the same time, and
    returning a value of the same type

    Parameter seq: the sequence to fold
    Precondition: seq is a sequence (tuple, string, etc.) whose elements are the
    same type as that returned by f

    Parameter value: the initial starting value
    Precondition: value has the same type as the return type of f
    """
    accum = value
    seq = seq[::-1]
    for x in seq:
        accum = f(x, accum)
    return accum


# result = fold_left(add, (4,), 0)
# print(result)
# # introcs.assert_equals(4, result)
# result = fold_left(sub, (), 2)
# print(result)
# #   introcs.assert_equals(2, result)
# result = fold_left(add, (4,), 0)
# print(result)
# #   introcs.assert_equals(4, result)

# result = fold_left(sub, (4,), 0)
# print(result)
# #   introcs.assert_equals(-4, result)
#
# result = fold_left(sub, (4,), 2)
# print(result)
# #   introcs.assert_equals(-2, result)
#
# result = fold_left(add, (1, 2, 3, 4), 0)
# print(result)
# #   introcs.assert_equals(10, result)
#
# result = fold_left(sub, (1, 2, 3, 4), 0)
# print(result)
# #   introcs.assert_equals(-10, result)
#
# result = fold_left(sub, (-1, -2, -3, -4), 0)
# print(result)
# #   introcs.assert_equals(10, result)