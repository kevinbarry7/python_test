"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Kevin Barry
Date:   April 18th 2020
"""

import introcs
import currency


def test_before_space():
    """Test procedure for before_space"""
    print("Testing before_space")

    result = currency.before_space('Hello World')
    introcs.assert_equals('Hello', result)
    result = currency.before_space(' HelloWorld')
    introcs.assert_equals('', result)
    result = currency.before_space('HelloWorld  ')
    introcs.assert_equals('HelloWorld', result)
    result = currency.before_space('Hello World Again ')
    introcs.assert_equals('Hello', result)


def test_after_space():
    """Test procedure for after_space"""
    print("Testing after_space")

    result = currency.after_space('Hello  World')
    introcs.assert_equals(' World', result)
    result = currency.after_space('Hello World')
    introcs.assert_equals('World', result)
    result = currency.after_space('HelloWorld ')
    introcs.assert_equals('', result)
    result = currency.after_space(' Hello World')
    introcs.assert_equals('Hello World', result)


def test_first_inside_quotes():
    """Test procedure for first_inside_quotes"""
    print("Testing first_inside_quotes")

    result = currency.first_inside_quotes('A B "C D" E')
    introcs.assert_equals('C D', result)
    result = currency.first_inside_quotes('A "B C" D "EF" G')
    introcs.assert_equals('B C', result)
    result = currency.first_inside_quotes('""')
    introcs.assert_equals('', result)
    result = currency.first_inside_quotes('"B"')
    introcs.assert_equals('B', result)


def test_get_src():
    """Test procedure for get_src"""
    print("Testing get_src")

    result = currency.get_src('{"success": true, "src": "2 United States Dollars",\
    "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)
    result = currency.get_src('{"success": true, "src":"2 United States Dollars",\
    "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)
    result = currency.get_src('{"success":false,"src":"",\
    "dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)
    result = currency.get_src('{"success":false,"src": "",\
    "dst":"","error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_get_dst():
    """Test procedure for get_dst"""
    print("Testing get_dst")

    result = currency.get_dst('{"success": true, "src": "2 United States Dollars",\
    "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)
    result = currency.get_dst('{"success": true, "src": "2 United States Dollars",\
    "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)
    result = currency.get_dst('{"success":false,"src":"","dst":"",\
    "error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)
    result = currency.get_dst('{"success":false,"src":"","dst": "",\
    "error":"Source currency code is invalid."}')
    introcs.assert_equals('', result)


def test_has_error():
    """Test procedure for has_error"""
    print("Testing has_error")

    result = currency.has_error('{"success": true, "src": "2 United States Dollars",\
    "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_false(result)
    result = currency.has_error('{"success":true, "src": "2 United States Dollars",\
    "dst": "1.772814 Euros", "error":""}')
    introcs.assert_false(result)
    result = currency.has_error('{"success":false,"src":"","dst":"",\
    "error":"Source currency code is invalid."}')
    introcs.assert_true(result)
    result = currency.has_error('{"success":false,"src":"","dst":"",\
    "error": "Source currency code is invalid."}')
    introcs.assert_true(result)


def test_service_response():
    """Test procedure for service_response"""
    print("Testing service_response")

    result = currency.service_response('USD', 'EUR', 2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars", "dst": "2.2160175 Euros", "error": ""}', result)
    result = currency.service_response('USA', 'EUR', 2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate for currency USA is not present."}', result)
    result = currency.service_response('USD', 'EUA', 2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "The rate for currency EUA is not present."}', result)
    result = currency.service_response('USD', 'EUR', -2.5)
    introcs.assert_equals('{"success": true, "src": "-2.5 United States Dollars", "dst": "-2.2160175 Euros", "error": ""}', result)


def test_iscurrency():
    """Test procedure for iscurrency"""
    print("Testing iscurrency")
    result = currency.iscurrency('USD')
    introcs.assert_true(result)
    result = currency.iscurrency('JPD')
    introcs.assert_false(result)


def test_exchange():
    """Test procedure for exchange"""
    print("Testing exchange")
    result = currency.exchange('USD', 'EUR', 2.5)
    introcs.assert_floats_equal(2.2160175, result)
    result = currency.exchange('USD', 'EUR', -2)
    introcs.assert_floats_equal(-1.772814, result)


test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()


print("All tests completed successfully.")




