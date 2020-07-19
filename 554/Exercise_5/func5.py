"""
A function to check the validity of a numerical string

Author: YOUR NAME HERE
Date: THE DATE HERE
"""
import introcs


def valid_format(s):
    """
    Returns True if s is a valid numerical string; it returns False otherwise.

    A valid numerical string is one with only digits and commas, and commas only
    appear at every three digits.  In addition, a valid string only starts with
    a 0 if it has exactly one character.

    Pay close attention to the precondition, as it will help you (e.g. only numbers
    < 1,000,000 are possible with that string length).

    Examples:
        valid_format('12') returns True
        valid_format('apple') returns False
        valid_format('1,000') returns True
        valid_format('1000') returns False
        valid_format('10,00') returns False
        valid_format('0') returns True
        valid_format('012') returns False

    Parameter s: the string to check
    Precondition: s is nonempty string with no more than 7 characters
    """
    assert type(s) == str, 'Precondition violation - non-string type'
    assert 1 <= len(s) < 8, 'Precondition violation - length of s'
    if introcs.isalpha(s):
        return False
    elif introcs.isnumeric(s) and len(s) < 2:
        return True
    elif introcs.isnumeric(s) and len(s) < 4:
        return no_comma(s) and is_zero_first(s)
    elif introcs.isalpha(s):
        return False
    elif last_three(s) and comma(s) and is_zero_first(s) and place_three(s):
        return True
    else:
        return False


def no_comma(s):
    num = introcs.find_str(s, ',')
    if num == -1:
        return True
    else:
        return False


def is_zero_first(s):
    if s[0] == '0':
        return False
    else:
        return True


def comma(s):
    if introcs.find_str(s, ','):
        if s[-4] == ',':
            return True
        else:
            return False


def last_three(s):
    last = s[-3:]
    if introcs.isnumeric(last):
        return True
    else:
        return False
    

def place_three(s):
    three = s[-5]
    if introcs.isnumeric(three):
        return True
    else:
        return False


result = valid_format('a,123')
print(result)
# print(introcs.isalpha(','))
# print(last_three('1,000'))
