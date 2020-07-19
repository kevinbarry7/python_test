"""
Functions for parsing time values and determining daylight hours.

Both of these functions will be used in the main project.  You should hold on to them.

Author: Kevin Barry
Date:   June 27, 2020
"""
import pytz
from dateutil.parser import *
import datetime
from pytz import *


def str_to_time(timestamp, tz=None):
    """
    Returns the datetime object for the given timestamp (or None if stamp is invalid)

    This function should just use the parse function in dateutil.parser to
    convert the timestamp to a datetime object.  If it is not a valid date (so
    the parser crashes), this function should return None.

    If the timestamp has a timezone, then it should keep that timezone even if
    the value for tz is not None.  Otherwise, if timestamp has no timezone and
    tz if not None, this this function will assign that timezone to the datetime
    object.

    The value for tz can either be a string or a time OFFSET. If it is a string,
    it will be the name of a timezone, and it should localize the timestamp. If
    it is an offset, that offset should be assigned to the datetime object.

    Parameter timestamp: The time stamp to convert
    Precondition: timestamp is a string

    Parameter tz: The timezone to use (OPTIONAL)
    Precondition: tz is either None, a string naming a valid time zone,
    or a time zone OFFSET.
    """
    # HINT: Use the code from the previous exercise and update the timezone
    # Use localize if timezone is a string; otherwise replace the timezone if not None

    try:
        result = parse(timestamp)
        if result.tzinfo is None and tz is None:
            return result
        elif result.tzinfo is None and type(tz) == str:
            time1 = pytz.timezone(tz)
            e = time1.localize(result)
            return e
        elif result.tzinfo is not None and tz is None:
            return result
        elif result.tzinfo is None and tz is not None:
            g = result.replace(tzinfo=tz)
            return g
        elif result.tzinfo is not None and tz is not None:
            h = result.replace()
            return h
    except ValueError:
        return None


def daytime(time, daycycle):
    """
    Returns true if the time takes place during the day.

    A time is during the day if it is after sunrise but before sunset, as
    indicated by the daycycle dicitionary.

    A daycycle dictionary has keys for several years (as int).  The value for
    each year is also a dictionary, taking strings of the form 'mm-dd'.  The
    value for that key is a THIRD dictionary, with two keys "sunrise" and
    "sunset".  The value for each of those two keys is a string in 24-hour
    time format.

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

    In addition, the daycycle dictionary has a key 'timezone' that expresses the
    timezone as a string. This function uses that timezone when constructing
    datetime objects from this set.  If the time parameter does not have a timezone,
    we assume that it is in the same timezone as the daycycle dictionary

    Parameter time: The time to check
    Precondition: time is a datetime object

    Parameter daycycle: The daycycle dictionary
    Precondition: daycycle is a valid daycycle dictionary, as described above
    """
    # HINT: Use the code from the previous exercise to get sunset AND sunrise
    # Add a timezone to time if one is missing (the one from the daycycle)

    try:

        tz_cycle = daycycle['timezone']
        if time.tzinfo is not None:
            year1 = time.strftime('%Y')
            date1 = time.strftime('%m-%d')
            sunrisetime = daycycle[year1][date1]['sunrise']
            sunsettime = daycycle[year1][date1]['sunset']
            y = year1 + '-' + date1
            y1 = datetime.datetime.strptime(y, '%Y-%m-%d')
            y3 = datetime.datetime.strptime(sunrisetime, '%H:%M').time()
            y2 = datetime.datetime.combine(y1, y3)
            x = y2.isoformat()

            y4 = datetime.datetime.strptime(sunsettime, '%H:%M').time()
            y5 = datetime.datetime.combine(y1, y4)
            x1 = y5.isoformat()
            back_sunrise = str_to_time(x, tz_cycle)
            back_sunset = str_to_time(x1, tz_cycle)
            if back_sunrise < time < back_sunset:
                return True
            else:
                return False

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

# input = '2016-05-12'
# result = str_to_time(input)
# print(result)
#
# input = '16:23'
# result = str_to_time(input)
# print(result)
#
# input = '16:23-4:00'
# result = str_to_time(input)
# print(result)
#
# input = '2016-05-12T16:23-4:00'
# result = str_to_time(input)
# print(result)
#
input = '2016-05-12T16:23'
correct = parse(input + '-4:00')
print(correct)
result = str_to_time(input, correct.tzinfo)
print(result)

input = '2016-05-12T16:23'
central = 'America/Chicago'
correct = timezone(central).localize(parse(input))
print(type(correct))
result = str_to_time(input, central)
print(result)