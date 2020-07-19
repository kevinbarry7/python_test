"""
Functions for parsing time values from text.

While these functions are similar to functions found in the assignment, they
are missing timezone information.  The next exercise will modify these
functions to make them compatible with the assignment.

Author: Kevin Barry
Date:   June 24, 2020
"""
from dateutil.parser import *
import datetime


def str_to_time(timestamp):
    """
    Returns the datetime object for the given timestamp (or None if the stamp is invalid)

    This function should just use the parse function in dateutil.parser to convert the
    timestamp to a datetime object.  If it is not a valid date (so the parser crashes),
    this function should return None.

    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string
    """
    # Hint: Use a try-except to return None if parsing fails
    try:
        res = parse(timestamp)
        print(res)
        return res
    except ValueError:
        print('None')
        return None


def sunset(date, daycycle):
    """
    Returns the sunset datetime (day and time) for the given date

    This function looks up the sunset from the given daycycle dictionary. If the
    daycycle dictionary is missing the necessary information, this function
    returns the value None.

    A daycycle dictionary has keys for several years (as int).  The value for each year
    is also a dictionary, taking strings of the form 'mm-dd'.  The value for that key
    is a THIRD dictionary, with two keys "sunrise" and "sunset".  The value for each of
    those two keys is a string in 24-hour time format.

    For example, here is what part of a daycycle dictionary might look like:

        "2015": {
            "01-01": {
                "sunrise": "07:35",
                "sunset":  "16:44"
            },
            "01-02": {
                "sunrise": "07:36",
                "sunset":  "16:45"
            },
            ...
        }

    Parameter date: The date to check
    Precondition: date is a date object

    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: ISO FORMAT IS 'yyyy-mm-ddThh:mm'.  For the sunrise value, construct a
    # string in ISO format and call str_to_time.

    try:
        date1 = date.strftime('%m-%d')
        year = date.strftime('%Y')
        sunsettime = daycycle[year][date1]['sunset']
        y = year + '-' + date1
        y1 = datetime.datetime.strptime(y, '%Y-%m-%d')
        y3 = datetime.datetime.strptime(sunsettime, '%H:%M').time()
        y2 = datetime.datetime.combine(y1, y3)
        x = y2.isoformat()
        print(x)

        if sunsettime == ' ':
            return None
        else:
            res = str_to_time(x)
            return res
    except KeyError:
        return None

daycycle = {
            "city": "Ithaca",
            "state": "New York",
            "latitude": "076-29W",
            "longitude": "42-26N",
            "timezone": "America/New_York",
            "2015": {
                "01-01": {
                    "sunrise": "07:35",
                    "sunset": "16:44"
                },
                "01-02": {
                    "sunrise": "07:36",
                    "sunset": "16:45"
                },
                "01-03": {
                    "sunrise": "07:36",
                    "sunset": "16:45"
                }
            }
        }


d = datetime.date(2015, 1, 3)
result = sunset(d, daycycle)
print(result)
# print("_____________")
# result = str_to_time('2016-04-15T10:15:45')
# print(result)

# result = str_to_time('2016-04-15')
# result = str_to_time('a-06-09')
