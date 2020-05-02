"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Kevin Barry
Date: April 18th 2020
"""

import introcs
APIKEY = '6gPsrpGIwEI6OeqAJ5YFBiZb8ACKoJ9RCRoSenEcJHke'


def before_space(s):
    """
    Returns the substring of s up to, but not including, the first space.

    Example: before_space('Hello World') returns 'Hello'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """

    assert type(s) == str, 'Precondition violation'
    assert introcs.count_str(s, " ") >= 1, 'Precondition violation'
    space_count = introcs.count_str(s, ' ')
    count = introcs.find_str(s, ' ')
    result = s[ : count]
    # print (result)
    return result


def after_space(s):
    """
    Returns the substring of s after the first space

    Example: after_space('Hello World') returns 'World'

    Parameter s: the string to slice
    Precondition: s is a string with at least one space in it
    """
    assert type(s) == str, 'Precondition violation'
    assert introcs.count_str(s, " ") >= 1, 'Precondition violation'
    # count = introcs.rfind_str(s,' ')
    count = introcs.find_str(s, ' ')
    # print(count)
    result = s[count + 1:]
    # print(result)
    return result


def first_inside_quotes(s):
    """
    Returns the first substring of s between two (double) quote characters

    Note that the double quotes must be part of the string.  So "Hello World" is a
    precondition violation, since there are no double quotes inside the string.

    Example: first_inside_quotes('A "B C" D') returns 'B C'
    Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only
    picks the first such substring.

    Parameter s: a string to search
    Precondition: s is a string with at least two (double) quote characters inside
    """

    assert type(s) == str, 'Precondition violation'
    assert introcs.count_str(s, '"') >= 2, 'Precondition violation'

    count1 = introcs.find_str(s, '"')
    # print(count1)
    count2 = introcs.find_str(s, '"', count1 + 1)
    # print(count2)
    result = s[count1 + 1: count2]
    # print(result)
    return result


def get_src(json):
    """
    Returns the src value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"src"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '2 United States Dollars' (not '"2 United States Dollars"').
    On the other hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    assert type(json) == str, 'Precondition violation'

    colon1 = introcs.index_str(json, ':')
    colon2 = introcs.index_str(json, ':', colon1 + 1)

    count1 = introcs.find_str(json, '"', colon2)
    count2 = introcs.find_str(json, '"', count1 + 1)
    result = json[count1 + 1:count2]
    return result


def get_dst(json):
    """
    Returns the dst value in the response to a currency query.

    Given a JSON string provided by the web service, this function returns the string
    inside string quotes (") immediately following the substring '"dst"'. For example,
    if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
    hand if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns the empty string.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    assert type(json) == str, 'Precondition violation'

    colon1 = introcs.index_str(json, ':')
    colon2 = introcs.index_str(json, ':', colon1 + 1)
    colon3 = introcs.index_str(json, ':', colon2 + 1)

    count1 = introcs.find_str(json, '"', colon3)
    count2 = introcs.find_str(json, '"', count1 + 1)
    result = json[count1 + 1:count2]
    return result


def has_error(json):
    """
    Returns True if the response to a currency query encountered an error.

    Given a JSON string provided by the web service, this function returns True if the
    query failed and there is an error message. For example, if the json is

        '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

    then this function returns True (It does NOT return the error message
    'Source currency code is invalid'). On the other hand if the json is

        '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

    then this function returns False.

    The web server does NOT specify the number of spaces after the colons. The JSON

        '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'

    is also valid (in addition to the examples above).

    Parameter json: a json string to parse
    Precondition: json a string provided by the web service (ONLY enforce the type)
    """

    assert type(json) == str, 'Precondition violation'

    colon1 = introcs.index_str(json, ':')
    colon2 = introcs.index_str(json, ':', colon1 + 1)
    colon3 = introcs.index_str(json, ':', colon2 + 1)
    colon4 = introcs.index_str(json, ':', colon3 + 1)

    count1 = introcs.find_str(json, '"', colon4)
    count2 = introcs.find_str(json, '"', count1 + 1)
    error = json[count1 + 1:count2]
    # print(error)
    result = bool(error)
    return result


def service_response(src, dst, amt):
    """
    Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the currency dst. The response
    should be a string of the form

        '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

    where the values src-amount and dst-amount contain the value and name for the src
    and dst currencies, respectively. If the query is invalid, both src-amount and
    dst-amount will be empty, and the error message will not be empty.

    There may or may not be spaces after the colon.  To test this function, you should
    chose specific examples from your web browser.

    Parameter src: the currency on hand
    Precondition src is a nonempty string with only letters

    Parameter dst: the currency to convert to
    Precondition dst is a nonempty string with only letters

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """

    assert type(src) == str and introcs.isalpha(src), 'Precondition violation'
    assert type(dst) == str and introcs.isalpha(dst), 'Precondition violation'
    assert type(amt) == float or type(amt) == int, 'Precondition violation'


    #q = 'https://ecpyfac.ecornell.com/python/currency/fixed?src=USD&dst=EUR&amt=2.5&key=a1b2c3d4'
    q = 'https://ecpyfac.ecornell.com/python/currency/fixed?'
    q += 'src=' + src
    q += '&dst=' + dst
    q += '&amt=' + str(amt)
    #q += '&key=a1b2c3d4'
    q += '&key=' + APIKEY
    response = introcs.urlread(q)
    return response


def iscurrency(a):
    """
    Returns True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a nonempty string with only letters
    """
    assert type(a) == str and introcs.isalpha(a), 'Precondition violation'

    json = service_response(a, a, 0.0)
    # print(json)
    q = has_error(json)
    # print(q)
    # print (type(q))
    q = not q
    # print(q)
    return q


def exchange(src, dst, amt):
    """
    Returns the amount of currency received in the given exchange.

    In this exchange, the user is changing amt money in currency src to the currency
    dst. The value returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter src: the currency on hand
    Precondition src is a string for a valid currency code

    Parameter dst: the currency to convert to
    Precondition dst is a string for a valid currency code

    Parameter amt: amount of currency to convert
    Precondition amt is a float or int
    """

    assert type(src) == str and iscurrency(src), 'Precondition violation'
    assert type(dst) == str and iscurrency(dst), 'Precondition violation'
    assert type(amt) == float or type(amt) == int, 'Precondition violation'

    json = service_response(src, dst, amt)
    # print(json)
    conv_amt = get_dst(json)
    # print(conv_amt)
    dst_amt = before_space(conv_amt)
    # print(dst_amt)
    # print(type(dst_amt))
    dst_amt = float(dst_amt)
    # print(type(dst_amt))
    return dst_amt

