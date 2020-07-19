"""
Module providing utility functions for this project.

These functions are general purpose utilities used by other modules in this project.
Some of these functions were exercises in early course modules and should be copied
over into this file.

The preconditions for many of these functions are quite messy.  While this makes writing
the functions simpler (because the preconditions ensure we have less to worry about),
enforcing these preconditions can be quite hard. That is why it is not necessary to
enforce any of the preconditions in this module.

Author: Kevin Barry
Date: July 1, 2020
"""
import csv
import json
from dateutil.parser import *
import datetime
import pytz
from datetime import date


def read_csv(filename):
    """
    Returns the contents read from the CSV file filename.

    This function reads the contents of the file filename and returns the contents as
    a 2-dimensional list. Each element of the list is a row, with the first row being
    the header. Cells in each row are all interpreted as strings; it is up to the
    programmer to interpret this data, since CSV files contain no type information.

    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file
    is a valid CSV file
    """
    result = []
    filein = open(filename)

    wrapper = csv.reader(filein)
    for row in wrapper:
        result.append(row)
    filein.close()
    return result


def write_csv(data, filename):
    """
    Writes the given data out as a CSV file filename.

    To be a proper CSV file, data must be a 2-dimensional list with the first row
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.

    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a  2-dimensional list of strings

    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """
    filein = open(filename, 'w')

    wrapper = csv.writer(filein)
    for row in data:
        wrapper.writerow(row)
    filein.close()


def read_json(filename):
    """
    Returns the contents read from the JSON file filename.

    This function reads the contents of the file filename, and will use the json module
    to covert these contents in to a Python data value.  This value will either be a
    a dictionary or a list.

    Parameter filename: The file to read
    Precondition: filename is a string, referring to a file that exists, and that file
    is a valid JSON file
    """
    file = open(filename)
    text = file.read()
    data = json.loads(text)
    file.close()
    return data


def str_to_time(timestamp,tz=None):
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


def daytime(time,daycycle):
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


def get_for_id(id, table):
    """
    Returns (a copy of) a row of the table with the given id.

    Table is a two-dimensional list where the first element of each row is an identifier
    (string).  This function searches table for the row with the matching identifier and
    returns a COPY of that row. If there is no match, this function returns None.

    This function is useful for extract rows from a table of pilots, a table of instructors,
    or even a table of planes.

    Parameter id: The id of the student or instructor
    Precondition: id is a string

    Parameter table: The 2-dimensional table of data
    Precondition: table is a non-empty 2-dimension list of strings
    """
    for rows in table:
        if rows[0] == id:
            return rows


def get_certification(takeoff,student):
    student_cert = -1
    classes = student[3:7]
    for i in range(len(classes)-1, -1, -1):
        if classes[i] == '':
            continue
        else:
            # type(classes[i]) == str:
            date1 = parse(classes[i])
            if takeoff > date1 and i == 3:
                student_cert = 3
                return student_cert
            elif takeoff > date1 and i == 2:
                student_cert = 2
                return student_cert
            elif takeoff > date1 and i == 1:
                student_cert = 1
                return student_cert
            elif takeoff > date1 and i == 0:
                student_cert = 0
                return student_cert
    return student_cert


def has_instrument_rating(takeoff, student):
    print(type(student[7]))
    if not student[7]:
        return False
    else:
        instrument_date = parse(student[7])
        print(type(instrument_date))
        if isinstance(takeoff, str):
            g = parse(takeoff)
            if g > instrument_date:
                return True
        else:
            print(type(takeoff))
            if takeoff > instrument_date:
                return True
            else:
                return False


def bad_visibility(visibility, minimum):
    feetpermile = 5280
    # if visibility['visibility'] == 'unavailable':
    #     result = True
    if visibility['units'] == 'FT':
        minimum = minimum * feetpermile
        if minimum > visibility['minimum']:
            result = True
        else:
            result = False
    elif visibility['units'] == 'SM':
        if minimum > visibility['prevailing']:
            result = True
        else:
            result = False
    return result


result = bad_visibility({'prevailing': 8.0, 'units': 'SM'}, 0.75)
print(result)

weather = {
        "visibility": {
            "prevailing": 10560.0,
            "minimum": 6000.0,
            "maximum": 10560.0,
            "units": "FT"
        }
}
weather1 = {
        "visibility": {
            "prevailing": 2.0,
            "units": "SM"
        }
}

result = read_csv('students.csv')
id = 'S00304'
student = get_for_id(id, result)

takeoff_datetime = datetime.datetime(2019, 9, 25, 13, 15, 45)
takeoff_str = takeoff_datetime.isoformat()


# a = get_certification(takeoff, student)
# print(a)

# b = has_instrument_rating(takeoff_str, student)
# print('_______')
# print(b)

# results = read_csv('minimums.csv')
# print(results)

# result = bad_visibility(weather, 1.5)
# print(result)


