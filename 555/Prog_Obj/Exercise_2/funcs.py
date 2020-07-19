"""
Module demonstrating how to write functions with objects.

This module contains two versions of the same function.  One version returns a new
value, while other modifies one of the arguments to contain the new value.

Author: Kevin Barry
Date: May 30, 2020
"""
import clock


def add_time1(time1, time2):
    """
    Returns the sum of time1 and time2 as a new Time object

    DO NOT ALTER time1 or time2, even though they are mutable

    Examples:
        The sum of 12hr 13min and 13hr 12min is 25hr 25min
        The sum of 1hr 59min and 3hr 2min is 4hr 1min

    Parameter time1: the starting time
    Precondition: time1 is a Time object

    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    hours1 = time1.hours
    print(type(hours1))
    mins1 = time1.minutes

    hours2 = time2.hours
    mins2 = time2.minutes

    hours3 = hours1 + hours2
    mins3 = mins1 + mins2
    if mins3 >= 60:
        mins3 = mins3 - 60
        hours3 = hours3 + 1
    else:
        mins3 = mins3

    result = clock.Time(hours3, mins3)
    return result


def add_time2(time1, time2):
    """
    Modifies time1 to be the sum of time1 and time2

    DO NOT RETURN a new time object.  Modify the object time1 instead.

    Examples:
        The sum of 12hr 13min and 13hr 12min is 25hr 25min
        The sum of 1hr 59min and 3hr 2min is 5hr 1min

    Parameter time1: the starting time
    Precondition: time1 is a Time object

    Parameter time2: the time to add
    Precondition: time2 is a Time object
    """
    hours1 = time1.hours
    mins1 = time1.minutes

    hours2 = time2.hours
    mins2 = time2.minutes

    hours1 = hours1 + hours2
    mins1 = mins1 + mins2
    if mins1 >= 60:
        mins1 = mins1 - 60
        hours1 = hours1 + 1
    else:
        mins1 = mins1

    print(hours1)
    print(mins1)
    time1.minutes = mins1
    time1.hours = hours1


time1 = clock.Time(12, 13)
time2 = clock.Time(1, 12)
result = add_time1(time1, time2) # return the result
print(result)

add_time2(time1, time2) # no return, just modify the time1 parameter

