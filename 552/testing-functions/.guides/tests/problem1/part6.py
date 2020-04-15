#!/usr/local/bin/python3
"""
Assess part 6, the final verification pass

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step6(file):
    """
    Checks all parts are ready for submission.
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_docstring(file,0)
    if not result[0]:
        result = verifier.grade_testcases(file,1)
    if not result[0]:
        result = verifier.grade_function(file,0)
    if not result[0]:
        print("The modules 'tests' and 'funcs' look correct.")
    return result[0]

if __name__ == '__main__':
    sys.exit(check_step6('tests.py'))