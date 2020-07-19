"""
Functions demonstrating string methods.

Neither this module nor any of these functions should import the introcs module.
In addition, you are not allowed to use loops or recursion in either function.

Author: Kevin Barry
Date: May 30, 2020
"""


def first_in_parens(s):
    """
    Returns: The substring of s that is inside the first pair of parentheses.

    The first pair of parenthesis consist of the first instance of character
    '(' and the first instance of ')' that follows it.

    Examples:
        first_in_parens('A (B) C') returns 'B'
        first_in_parens('A (B) (C)') returns 'B'
        first_in_parens('A ((B) (C))') returns '(B'

    Parameter s: a string to check
    Precondition: s is a string with a matching pair of parens '()'.
    """
    first_parens = s.find('(')
    second_parens = s.find(')', first_parens + 1)
    result = s[first_parens + 1: second_parens]

    return result



def isnetid(s):
    """
    Returns True if s is a valid Cornell netid.

    Cornell network ids consist of 2 or 3 lower-case initials followed by a
    sequence of digits.

    Examples:
        isnetid('wmw2') returns True
        isnetid('2wmw') returns False
        isnetid('ww2345') returns True
        isnetid('w2345') returns False
        isnetid('WW345') returns False

    Parameter s: the string to check
    Precondition: s is a string
    """
    assert type(s) == str

    s2 = s[:2]
    s3 = s[:3]
    s4 = s[2:]
    s5 = s[3:]

    if s2.islower() and s2.isalpha() and s4.isnumeric():
        return True
    elif s3.islower() and s3.isalpha() and s5.isnumeric():
        return True
    else:
        return False




# output = first_in_parens('ABC((D)')
# print(output)
# output = first_in_parens('A ) B (C) D')
# print(output)

ans = isnetid('#mw2') # returns True
print(ans)
ans1 = isnetid('#w999') # returns False
print(ans1)
isnetid('ww2345') # returns True
isnetid('w2345') # returns False
isnetid('WW345') # returns False