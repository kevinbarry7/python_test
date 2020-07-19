"""
A simple function comparing datetime objects.

Author: Kevin Barry
Date:   June 22, 2020
"""
import datetime


def is_before(d1, d2):
    """
    Returns True if event d1 happens before d2.

    Values d1 and d2 can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day.

    Parameter d1: The first event
    Precondition: d1 is EITHER a date object or a datetime object

    Parameter d2: The first event
    Precondition: d2 is EITHER a date object or a datetime object
    """
    # HINT: Check the type of d1 or d2. If not a datetime, convert it for comparison

    if 'datetime.datetime' not in str(type(d1)):
        d1time = datetime.time(0, 0)
        x = datetime.datetime.combine(d1, d1time)
    else:
        x = d1

    if 'datetime.datetime' not in str(type(d2)):
        d2time = datetime.time(0, 0)
        y = datetime.datetime.combine(d2, d2time)
    else:
        y = d2

    if x < y:
        return True
    else:
        return False


d1 = datetime.date(2019, 10, 12)
d2 = datetime.date(2019, 10, 15)
d3 = datetime.datetime(2019, 10, 12, 9, 45, 15)

result = is_before(d1, d3)
print(result)