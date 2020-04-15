"""
A test script to test the module funcs.py

Author: Kevin Barry
Date: April 5, 2020
"""
import introcs      # For assert_equals and assert_true
import funcs        # This is what we are testing


# Script Code

def test_has_a_vowel():
    """
    Test procedure for has_a_vowel
    """
    print("Testing has_a_vowel")
    
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
    
    

def test_has_y_vowel():
    """
    Test procedure for has_y_vowel
    """
    
    result = funcs.has_y_vowel('tony')
    introcs.assert_equals(True, result)
    
    result = funcs.has_y_vowel('constantly')
    introcs.assert_equals(True, result)
    
    result = funcs.has_y_vowel('ayyy')
    introcs.assert_equals(True, result)
    
    result = funcs.has_y_vowel('my')
    introcs.assert_equals(True, result)
    
    print("Testing has_y_vowel")

# Script Code
test_has_a_vowel()
test_has_y_vowel()

print('Module funcs is working correctly')
