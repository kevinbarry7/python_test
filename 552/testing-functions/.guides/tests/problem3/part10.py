#!/usr/local/bin/python3
"""
Assess part 10, the second bug fix

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step10(file):
    """
    Checks that the first bug is fixed.
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_function(file,1)
    if not result[0]:
        print("The second bug fix for 'replace_first' looks correct.")
    return result[0]

if __name__ == '__main__':
    sys.exit(check_step10('tests.py'))
