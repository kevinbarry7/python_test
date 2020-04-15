#!/usr/local/bin/python3
"""
Assess part 5, adding the watches

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step5(file):
    """
    Checks that the watches are okay
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.verify_watches(file)
    if not result:
        print("The watches (print statements) in 'replace_first' look correct.")
    return result

if __name__ == '__main__':
    sys.exit(check_step5('tests.py'))
