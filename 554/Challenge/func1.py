"""
A function to find all instances of a substring.

This function is not unlike a 'find-all' option that you might see in a text editor.

Author: Kevin Barry
Date: May 25, 2020
"""
import introcs


def findall(text, sub):
    """
    Returns the tuple of all positions of substring sub in text.

    If sub does not appears anywhere in text, this function returns the empty tuple ().

    Examples:
        findall('how now brown cow','ow') returns (1, 5, 10, 15)
        findall('how now brown cow','cat') returns ()
        findall('jeeepeeer','ee') returns (1,2,5,6)

    Parameter text: The text to search
    Precondition: text is a string

    Parameter sub: The substring to search for
    Precondition: sub is a nonempty string
    """
    assert sub != '', 'sub must be a nonempty string'
    i = 0
    result = ()

    if introcs.count_str(text, sub) > 0:
        while i < len(text):
            pos = introcs.find_str(text, sub, i)
            print('pos = ' + str(pos))
            i = pos + 1
            print('i =' + str(i))
            result = result + (pos,)
    else:
        return result
    print(result)


findall('how now brown cow', 'ow')
# introcs.assert_equals((1, 5, 10, 15), result)

# findall('how now brown cow', 'brown')
# introcs.assert_equals((8,), result)

# findall('how now brown cow', 'cat')
# introcs.assert_equals((), result)

# result = func.findall('jeeepeeer', 'ee')
# introcs.assert_equals((1, 2, 5, 6), result)

# findall('', 'a')
# introcs.assert_equals((), result)

# findall('the cat in the hat had a sad', 'a')
# introcs.assert_equals((5, 16, 20, 23, 26), result)