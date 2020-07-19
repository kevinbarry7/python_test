"""
Functions for working with datetime objects.

Author: Kevin Barry
Date:   June 21, 2020
"""
import datetime


def christmas_day(year):
    """
    Returns ISO day of the week for Christmas in the given year.

    The ISO day is an integer between 1 and 7.  It is 1 for Monday, 7 for Sunday
    and the appropriate number for any day in-between.

    Parameter year: The year to check for Christmas
    Precondition: years is an int > 0 (and a year using the Gregorian calendar)
    """
    # HINT: Make a date object and use the isoweekday method

    month = 12
    day = 25

    d = datetime.date(year, month, day)
    print(str(d))
    cday = d.isoweekday()
    return cday


def iso_str(d, t):
    """
    Returns the ISO formatted string of data and time together.

    When combining, the time must be accurate to the microsecond.

    Parameter d: The month-day-year
    Precondition: d is a date object

    Parameter t: The time of day
    Precondition: t is a time object
    """
    # HINT: Combine date and time into a datetime and use isoformat

    res = str(d)
    res1 = str(t)
    res2 = datetime.datetime.combine(d, t)
    res3 = res2.isoformat()
    return res3


result = christmas_day(2020)
print(result)

d = datetime.date(2019, 8, 6)
t = datetime.time(14, 22, 34, 1000)
iso_str(d, t)
