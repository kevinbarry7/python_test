"""
A function to test for floats in European format

Author: Kevin Barry
Date: May 17, 2020
"""
import introcs


def iseurofloat(s):
    """
    Returns True if s is a float in European format.  Returns False otherwise.

    In European format, a comma is used in place of a decimal point.  So '12,5' stands
    for 12.5, '0,12' stands for 0.12 and so.  Formally, a string is in European format
    if it is of the form <d1>,<d2> where d1 and d2 are ints (and d2 >= 0).  See

        https://en.wikipedia.org/wiki/Decimal_separator

    for more information.

    This function does not recognize floats in scientific notation (e.g. '1e-2').

    Examples:
        iseurofloat('12,5') returns True
        iseurofloat('-12,5') returns True
        iseurofloat('12') returns False
        iseurofloat('12,-5') returns False
        iseurofloat(',5') returns False
        iseurofloat('apple') returns False
        iseurofloat('12,5.3') returns False
        iseurofloat('12,5,3') returns False
        iseurofloat('1e-2') returns False

    Parameter s: The string to check
    Precondition: s is a string
    """
    # You MAY NOT use conditionals anywhere in this function.

    try:
        x = introcs.index_str(s, ',')
        assert introcs.isint(s[x+1])
        n1 = s[:x]
        n2 = s[x+1:]
        y = int(n1)
        z = int(n2) >= 0
        return True
    except:
        return False


result = iseurofloat('12,5')
print(result)
result = iseurofloat('-12,5')
print(result)
result = iseurofloat('12')
print(result)
result = iseurofloat('12,-5')
print(result)
# result = iseurofloat(',5')
# print(result)
# result = iseurofloat('apple')
# print(result)
# result = iseurofloat('12,5.3')
# print(result)
# result = iseurofloat('12,5,3')
# print(result)
# result = iseurofloat('1e-2')
# print(result)
# result = iseurofloat(12,-5)
# print(result)