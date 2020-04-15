#!/usr/local/bin/python3
"""
Assess part 5, the first set of test cases

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step5(file):
    """
    Checks that the first test cases are okay
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_testcases(file,0)
    if not result[0]:
        print("The test cases for 'has_a_vowel' look correct.")
    return result[0]

if __name__ == '__main__':
    sys.exit(check_step5('tests.py'))