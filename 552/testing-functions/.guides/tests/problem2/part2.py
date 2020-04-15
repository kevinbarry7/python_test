#!/usr/local/bin/python3
"""
Assess part 2, the procedure print statements.

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import verifier
import sys


def check_step2(file):
    """
    Checks that the procedure print statements are okay
    
    Parameter file: The file to check
    Precondition: file is a string
    """
    result = verifier.grade_procedures(file,1)
    if not result[0]:
        print("The test procedures look correct.")
    return result[0]

if __name__ == '__main__':
    sys.exit(check_step2('tests.py'))
