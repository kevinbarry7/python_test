"""
Functions for simple reading to and writing from a file.

Author: Kevin Barry
Date:   June 17, 2020
"""
import os.path


def count_lines(filepath):
    """
    Returns the number of lines in the given file.

    Lines are separated by the '\n' character, which is standard for Unix files.

    Parameter filepath: The file to be read
    Precondition: filepath is a string with the FULL PATH to a text file
    """
    # HINT: Remember, you can use a file in a for-loop

    x = 0
    filein = open(filepath)
    for line in filein:
        x = x + 1
    filein.close()
    return x



def write_numbers(filepath, n):
    """
    Writes the numbers 0..n-1 to a file.

    Each number is on a line by itself.  So the first line of the file is 0,
    the second line is 1, and so on. Lines are separated by the '\n' character,
    which is standard for Unix files.  The last line (the one with the number
    n-1) should NOT end in '\n'

    Parameter filepath: The file to be written
    Precondition: filepath is a string with the FULL PATH to a text file

    Parameter n: The number of lines to write
    Precondition: n is an int > 0.
    """
    # HINT: You can only write strings to a file, so convert the numbers first

    filein = open(filepath, 'w')
    for n in range(0, n-1):
        print(n)
        filein.write(str(n) + '\n')

    filein.close()
    print(n + 1)
    fileout = open(filepath, 'a')
    fileout.write(str(n+1))
    fileout.close()




# filepath = os.path.join('files', 'readfile1.txt')
# result = count_lines(filepath)
# print(result)


filepath = os.path.join('files', 'readfile9.txt')
write_numbers(filepath, 5)
