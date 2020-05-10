"""
A function to search for the first vowel position

Author: Kevin Barry
Date: May 7, 2020
"""
import introcs


def first_vowel(s):
    """
    Returns the position of the first vowel in s; it returns len(s) if there are no vowels.

    We define the vowels to be the letters 'a','e','i','o', and 'u'.  The letter
    'y' counts as a vowel only if it is not the first letter in the string.

    Examples:
        first_vowel('hat') returns 1
        first_vowel('grrm') returns 4
        first_vowel('sky') returns 2
        first_vowel('year') returns 1

    Parameter s: the string to search
    Precondition: s is a nonempty string with only lowercase letters
    """
    result = len(s)

    if introcs.find_str(s, 'a') > -1:
        result = introcs.find_str(s, 'a')
    if -1 < introcs.find_str(s, 'e') < result:
        result = introcs.find_str(s, 'e')
    if -1 < introcs.find_str(s, 'i') < result:
        result = introcs.find_str(s, 'i')
    if -1 < introcs.find_str(s, 'o') < result:
        result = introcs.find_str(s, 'o')
    if -1 < introcs.find_str(s, 'u') < result:
        result = introcs.find_str(s, 'u')
    if -1 < introcs.find_str(s, 'y', 1) < result:
        result = introcs.find_str(s, 'y', 1)
    return result


result1 = first_vowel('yyeat')
print(result1)
