#!/usr/local/bin/python3
"""
Assess part 1, the procedure headers.

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step1(file):
    """
    Checks that the procedure headers are okay
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_docstring(file,0)
    if not result[0]:
        result = verifier.grade_procedures(file,0)
        if not result[0]:
            print("The procedure stubs look correct.")
    return result[0]

if __name__ == '__main__':
    sys.exit(check_step1('tests.py'))
