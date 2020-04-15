#!/usr/local/bin/python3
"""
Assess part 5, the bug fix.

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step5(file):
    """
    Checks that the bug fix is okay
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_function(file)
    if not result[0]:
        print("The bug fix looks correct.")
    return result[0]


if __name__ == '__main__':
    sys.exit(check_step5('tests.py'))
