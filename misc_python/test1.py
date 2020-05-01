"""
A test script to test the module func.py

Author: Kevin Barry
Date: April 5, 2020
"""
import introcs  # For assert_equals and assert_true
import funcs  # This is what we are testing


def test_replace_first():
    """
    Test procedure for replace_first
    """
    print('Testing replace_first')

    # Put your tests below this line

    result = funcs.replace_first('crane', 'a', 'o')
    introcs.assert_equals('crone', result)

    result = funcs.replace_first('poll', 'l', 'o')
    introcs.assert_equals('pool', result)

    result = funcs.replace_first('crane', 'cr', 'b')
    introcs.assert_equals('bane', result)

    result = funcs.replace_first('p', 'p', 'papa')
    introcs.assert_equals('papa', result)

    result = funcs.replace_first('jams', 's', 'es')
    introcs.assert_equals('james', result)

    # replace_first('crane','cr','b') returns 'bane'


# Script Code
# Do not write below this line
test_replace_first()
print('Module funcs is working correctly')
