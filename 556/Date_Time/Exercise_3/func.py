"""
A simple function computing time elapsed

Author: Kevin Barry
Date:   June 23, 2020
"""
import datetime


def past_a_week(d1, d2):
    """
    Returns True if event d2 happens at least a week (7 days) after d1.

    If d1 is after d2, or less than a week has passed, this function returns False.
    Values d1 and d2 can EITHER be date objects or datetime objects.If a date object,
    assume that it happens at midnight of that day.

    Parameter d1: The first event
    Precondition: d1 is EITHER a date objects or a datetime object

    Parameter d2: The first event
    Precondition: d2 is EITHER a date objects or a datetime object
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

    print(x)
    print(y)

    res = y - x
    print(res)
    res1 = res.days
    print(res1)

    if res1 >= 7:
        return True
    else:
        return False


d1 = datetime.date(2019, 10, 12)
d2 = datetime.date(2019, 10, 25)
d3 = datetime.date(2019, 10, 19)
d4 = datetime.datetime(2019, 10, 12, 9, 45, 15)
d5 = datetime.datetime(2019, 10, 19, 10, 15)
d6 = datetime.datetime(2019, 10, 19, 8, 30)

result = past_a_week(d4, d5)
print(result)