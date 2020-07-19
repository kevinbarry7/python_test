"""
Module with a function to write CSV files (using data in a 2D list)

This function will be used in the main project.  You should hold on to it.

Author: Kevin Barry
Date: June 20, 2020
"""
import csv


def write_csv(data,filename):
    """
    Writes the given data out as a CSV file filename.
    
    To be a proper CSV file, data must be a 2-dimensional list with the first row 
    containing only strings.  All other rows may be any Python value.  Dates are
    converted using ISO formatting. All other objects are converted to their string
    representation.
    
    Parameter data: The Python value to encode as a CSV file
    Precondition: data is a  2-dimensional list
    
    Parameter filename: The file to read
    Precondition: filename is a string representing a path to a file with extension
    .csv or .CSV.  The file may or may not exist.
    """

    filein = open(filename, 'w')

    wrapper = csv.writer(filein)
    for row in data:
        wrapper.writerow(row)
    filein.close()

FILE1 = [['STUDENT', 'AIRPLANE', 'INSTRUCTOR', 'TAKEOFF', 'LANDING', 'FILED', 'AREA'],
         ['S00309', '738GG', 'I076', '2015-01-12T09:00:00-05:00', '2015-01-12T11:00:00-05:00', 'VFR', 'Pattern'],
         ['S00308', '133CZ', 'I053', '2015-01-13T09:00:00-05:00', '2015-01-13T12:00:00-05:00', 'VFR', 'Practice Area'],
         ['S00324', '426JQ', 'I053', '2015-02-04T11:00:00-05:00', '2015-02-04T14:00:00-05:00', 'VFR', 'Cross Country'],
         ['S00319', '811AX', 'I072', '2015-02-06T13:00:00-05:00', '2015-02-06T15:00:00-05:00', 'VFR', 'Pattern'],
         ['S00321', '738GG', 'I072', '2015-02-08T10:00:00-05:00', '2015-02-08T13:00:00-05:00', 'VFR', 'Practice Area'],
         ['S00308', '811AX', 'I072', '2015-02-23T09:00:00-05:00', '2015-02-23T13:00:00-05:00', 'VFR', 'Cross Country']]

write_csv(FILE1, 'test1.csv')
