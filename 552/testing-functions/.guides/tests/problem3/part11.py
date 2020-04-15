#!/usr/local/bin/python3
"""
Assess part 11, the remaining test cases

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step11(file):
    """
    Checks that the third test case is okay.
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_testcases(file,3)
    if not result[0]:
        print("The remaining test cases looks correct.")
    return result[0]

if __name__ == '__main__':
    sys.exit(check_step11('tests.py'))