"""
A test script to test the module funcs.py

Author: Kevin Barry
Date: April 4, 2020
"""

import introcs      # For assert_equals
import funcs        # This is what we are testing

# Put your code below this line
result = funcs.has_a_vowel('aeiou')
introcs.assert_equals(True, result)

result = funcs.has_a_vowel('sat')
introcs.assert_equals(True, result)

result = funcs.has_a_vowel('eat')
introcs.assert_equals(True, result)

result = funcs.has_a_vowel('tamara')
introcs.assert_equals(True, result)

result = funcs.has_a_vowel('tom')
introcs.assert_equals(True, result)

result = funcs.has_a_vowel('umbrella')
introcs.assert_equals(True, result)

result = funcs.has_a_vowel('april')
introcs.assert_equals(True, result)

result = funcs.has_a_vowel('limit')
introcs.assert_equals(True, result)

result = funcs.has_a_vowel('reviewed')
introcs.assert_equals(True, result)

result = funcs.has_a_vowel('sequioia')
introcs.assert_equals(True, result)

# Do not write below this line
print('Module funcs is working correctly')
