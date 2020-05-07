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

    def first_vowel(s):

        result = len(s)

        if introcs.find_str(s, 'a') > -1:
            return introcs.find_str(s, 'a')
        if introcs.find_str(s, 'e') > -1:
            return introcs.find_str(s, 'e')
        if introcs.find_str(s, 'i') >= 0:
            return introcs.find_str(s, 'i')
        if introcs.find_str(s, 'o') >= 0:
            return introcs.find_str(s, 'o')
        if introcs.find_str(s, 'u') >= 0:
            return introcs.find_str(s, 'u')
        if introcs.find_str(s, 'y') > 0:
            return introcs.find_str(s, 'y')
        return result

    place = first_vowel('sss')
    print(place)
