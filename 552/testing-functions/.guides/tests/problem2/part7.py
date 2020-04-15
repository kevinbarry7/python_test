#!/usr/local/bin/python3
"""
Assess part 7, the test cases for has_y_vowel

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step7(file):
    """
    Checks that the remaining test cases are okay.
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_testcases(file,1)
    if not result[0]:
        print("All test cases look correct.")
    return result[0]

if __name__ == '__main__':
    sys.exit(check_step7('tests.py'))