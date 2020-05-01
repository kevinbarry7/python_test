
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