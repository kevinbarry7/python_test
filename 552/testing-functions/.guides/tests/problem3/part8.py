#!/usr/local/bin/python3
"""
Assess part 8, the third test case.

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step8(file):
    """
    Checks that the third test case is okay.
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_testcases(file,2)
    if not result[0]:
        print("The third test case looks correct.")
    return result[0]

if __name__ == '__main__':
    sys.exit(check_step8('tests.py'))