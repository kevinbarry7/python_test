"""
Module demonstrating immutable functions on dictionaries

All of these functions make use of accumulators.

Author: Kevin Barry
Date: June 10, 2020
"""


def average_grade(adict):
    """
    Returns the average grade among all students.

    The dictionary adict has netids for keys and numbers 0-100 for values.
    These represent the grades that the students got on the exam.  This function
    averages those grades and returns a value.

    Examples:
        average_grade({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns (55+90+86)/3 = 77
        average_grade({'wmw2' : 55}) returns 55
        average_grade({}) returns 0

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    accumulator = 0
    div = len(adict)
    if not bool(adict):
        result = 0.0
    else:
        for i in adict:
            accumulator = accumulator + adict[i]
        result = accumulator / div
    return result


def letter_grades(adict):
    """
    Returns a new dictionary with the letter grades for each student.

    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function returns a
    new dictionary with netids for keys and letter grades (strings) for values.

    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60
    is an F.

    Examples:
        letter_grades({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) returns
            {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        letter_grades({}) returns {}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """
    accumulator = {}
    for k, v in adict.items():
        if v >= 90:
            v = 'A'
            accumulator.update({k: v})
        elif v >= 80:
            v = 'B'
            accumulator.update({k: v})
        elif v >= 70:
            v = 'C'
            accumulator.update({k: v})
        elif v >= 60:
            v = 'D'
            accumulator.update({k: v})
        else:
            v = 'F'
            accumulator.update({k: v})


    print(accumulator)
    print(adict)


# result = average_grade({'wmw2' : 55, 'abc3' : 90, 'jms45': 86}) # returns (55+90+86)/3 = 77
# print(result)
# result = average_grade({}) # returns 0
# print(result)

letter_grades({'alan': 98, 'Kevin': 90})
letter_grades({'wmw2': 55, 'abc3': 90})