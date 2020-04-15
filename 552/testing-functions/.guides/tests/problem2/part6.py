#!/usr/local/bin/python3
"""
Assess part 6, the bug fix for has_a_vowel

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step6(file):
    """
    Checks that the first bug fix is okay
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_functions(file,0)
    if not result[0]:
        print("The bug fix for 'has_a_vowel' looks correct.")
    return result[0]

if __name__ == '__main__':
    sys.exit(check_step6('tests.py'))