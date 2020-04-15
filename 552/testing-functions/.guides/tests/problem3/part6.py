#!/usr/bin/env python
"""
Assess the third free-response question.

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
for pos in range(len(answer)):
    answer[pos] = answer[pos].strip()

while len(answer) > 0 and answer[0] == '':
    del answer[0]
while len(answer) > 0 and answer[-1] == '':
    del answer[-1]

result  = True
if len(answer) == 0:
    print('The answer should not be empty.')
    result = False
elif len(answer) != 12:
    print('The answer should take up twelve lines.')
    result = False
elif not 'Testing replace_first' in answer:
    print('The output is not correct.')
    result = False
elif not 'Quitting with Error' in answer:
    print('The output is not correct.')
    result = False
elif answer[0] != 'Testing replace_first':
    print('The output is not in the right order.')
    result = False
elif answer[1:5] != ['2','cr','ne','crone']:
    print("The output is missing the print statements added to 'replace_first'")
    result = False
elif answer[5:9] != ['3','pol','','polo']:
    print("The output is missing the print statements added to 'replace_first'")
    result = False
elif answer[-1] != "Quitting with Error":
    print('The output is not in the right order.')
    result = False

if result:
    print('Correct')
else:
    sys.exit(1)