"""
Module demonstrating mutable functions on dictionaries.

All of these functions modify their dictionary arguments.

Author: Kevin Barry
Date: June 11, 2020
"""


def letter_grades(adict):
    """
    Modifies the new dictionary to replace numerical grades with letter grades.

    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam. This function replaces
    all of the numerical grades with letter grades (strings) for values.

    Our cut-off is 90 for an A, 80 for a B, 70 for a C, 60 for a D. Anything below 60
    is an F.

    Examples:
        If a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}, letter_grades(a) changes
            a to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}.
        If a = {} letter_grades(a) changes a to {}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints
    """

    for k, v in adict.items():
        print(k)
        if v >= 90:
            adict[k] = 'A'
        elif v >= 80:
            adict[k] = 'B'
        elif v >= 70:
            adict[k] = 'C'
        elif v >= 60:
            adict[k] = 'D'
        elif v < 60:
            adict[k] = 'F'



def drop_below(adict, limit):
    """
    Deletes all students in the dictionary with grades below limit.

    The dictionary adict has netids for keys and numbers 0-100 for values. These
    represent the grades that the students got on the exam.

    Examples: Suppose a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}
        drop_below(a,60) changes a to {'abc3' : 90, 'jms45': 86}
        drop_below(a,90) changes a to {'abc3' : 90}
        drop_below(a,95) changes a to {}
        drop_below(a,50) leaves a unchanged as {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}

    Parameter adict: the dictionary of grades
    Precondition: adict is dictionary mapping strings to ints

    Paramater limit: the cut-off boundary
    Precondition: limit is a number (int or float)
    """
    # Hint: Create a list of netids to drop, and THEN drop them

    key_list = []

    for k,v in adict.items():
        if v < limit:
            key_list.append(k)
    print(key_list)
    for j in key_list:
        if j in adict:
            del adict[j]
    print(adict)


a = {'wmw2' : 55, 'abc3' : 90, 'jms45': 86}
drop_below(a,60) #  changes a to {'abc3' : 90, 'jms45': 86}



# a = {'wmw2': 55, 'abc3': 90, 'jms45': 86}
# letter_grades(a) #  changes a to {'wmw2' : 'F, 'abc3' : 'A', 'jms45': 'B'}
# print(a)
