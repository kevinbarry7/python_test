#!/usr/bin/env python
"""
Assess the second free-response question.

This file is insecurely available to students, but if they find it and modify it, they
really did not need this course.

Author: Walker M. White
Date:   July 1, 2019
"""
import os, requests, sys
import subprocess

answer  = os.environ['CODIO_FREE_TEXT_ANSWER']
#answer = sys.argv[1] if len(sys.argv) > 1 else ''

answer = answer.strip().split('\n')
answer = list(filter(lambda x : len(x) > 0, answer))

result  = True
if len(answer) != 3:
    print('The answer should be three non-empty lines.')
    result = False
elif not 'assert_equals' in answer[0]:
    print('The first line should be the an error from assert_equals.')
    result = False
elif answer[0].strip() != 'assert_equals: expected True but instead got False':
    print('The first line is incomplete.')
    result = False
elif answer[2].strip() == 'Quitting with Error.':
    print("The last line should not end with a period.")
    result = False
elif answer[2].strip() != 'Quitting with Error':
    print("The last line should be 'Quitting with Error'.")
    result = False

if result:
    print('Correct')
else:
    sys.exit(1)
