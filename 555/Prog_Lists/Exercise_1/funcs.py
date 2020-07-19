"""
Module demonstrating mutable list functions.

Neither of these functions should use for-lopps.  Instead, they should use
list methods.

Author: Kevin Barry
Date: June 4, 2020
"""


def put_in(alist, value):
    """
    Adds a value to a sorted list, resorting as necessary.

    Examples:
        If a = [0,2,3,4], put_in(a,1) makes a = [0,1,2,3,4]
        If a = [0,2,3,4], put_in(a,2) makes a = [0,2,2,3,4]
        If a = [], put_in(a,3) makes a = [3]

    Parameter a: The list to append to
    Precondition: a is a sorted list of a single type of element

    Parameter value: The value to append
    Precondition: value has the same type as the elements of a
    """
    x = alist
    x.append(value)
    x.sort()



def rotate(alist):
    """
    Rotates the contents of alist one element to the right.

    Rotating a list to the right pushes all elements to the right, and makes
    the previously last element the new first element.

    Examples:
        If a = [0,2,3,4], rotate(a) makes a = [4,0,2,3]
        If a = [1], rotate(a) makes a = [1]

    Parameter a: The list to rotate
    Precondition: a non-empty list
    """
    # Hint: Read the method description for insert
    x = alist
    if len(x) > 0:
        y = x.pop()
        x.insert(0, y)




alist = [0, 1, 2, 4]
put_in(alist, 3)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([0, 1, 2, 3, 4], alist)

result = put_in(alist, -1)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([-1, 0, 1, 2, 3, 4], alist)

result = put_in(alist, 2)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([-1, 0, 1, 2, 2, 3, 4], alist)
    #
result = put_in(alist, 0)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([-1, 0, 0, 1, 2, 2, 3, 4], alist)
    #
alist = []
result = put_in(alist, 0)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([0], alist)
    #
result = put_in(alist, 1)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([0, 1], alist)
    #
alist = ['a', 'aa', 'ab', 'b', 'ce']
result = put_in(alist, 'aab')
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals(['a', 'aa', 'aab', 'ab', 'b', 'ce'], alist)

print('Testing rotate()')

alist = [0, 1, 3, 5]
result = rotate(alist)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([5, 0, 1, 3], alist)
    #
result = rotate(alist)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([3, 5, 0, 1], alist)
    #
result = rotate(alist)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([1, 3, 5, 0], alist)
    #
result = rotate(alist)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([0, 1, 3, 5], alist)
    #
alist = [9]
result = rotate(alist)
print(alist)
    # introcs.assert_equals(None, result)
    # introcs.assert_equals([9], alist)

