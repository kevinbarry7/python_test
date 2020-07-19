"""
Module demonstrating immutable functions on nested lists.

All of these functions make use of accumulators that make new lists.

Author: Kevin Barry
Date: June 8, 2020
"""


def row_sums(table):
    """
    Returns a list that is the sum of each row in a table.

    This function assumes that table has no header, so each row has only numbers in it.

    Examples:
        row_sums([[0.1,0.3,0.5],[0.6,0.2,0.7],[0.5,1.1,0.1]]) returns [0.8, 1.5, 1.7]
        row_sums([[0.2,0.1],[-0.2,0.1],[0.2,-0.1],[-0.2,-0.1]]) returns [0.3, -0.1, 0.1, -0.3]

    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words,
        (1) table is a nested 2D list in row-major order,
        (2) each row contains only numbers, and
        (3) each row is the same length.
    """
    sum_list = []

    for row in table:
        sum = 0
        for item in row:
            sum = sum + item
        sum_list.append(sum)
    return sum_list


def crossout(table, row, col):
    """
    Returns a copy of the table, missing the given row and column.

    Examples:
        crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) returns [[1,3],[5,8]]
        crossout([[1,3,5],[6,2,7],[5,8,4]],0,0) returns [[2,7],[8,4]]
        crossout([[1,3],[6,2]],0,0) returns [[2]]
        crossout([[6]],0,0) returns []

    Parameter table: the nested list to process
    Precondition: table is a table of numbers.  In other words,
        (1) table is a nested 2D list in row-major order,
        (2) each row contains only numbers, and
        (3) each row is the same length.

    Parameter row: the row to remove
    Precondition: row is an index (int) for a row of table

    Parameter col: the column to remove
    Precondition: col is an index (int) for a column of table
    """
    result = []
    numrows = len(table)
    numcols = len(table[0])
    for m in range(numrows):
        list1 = []
        for n in range(numcols):
            if m != row and n != col:
                list1.append(table[m][n])
        if len(list1) > 0:
            result.append(list1)

    return result


# result = row_sums([[0.1,0.3,0.5],[0.6,0.2,0.7],[0.5,1.1,0.1]]) # returns [0.8, 1.5, 1.7]
# print(result)
result = crossout([[1,3,5],[6,2,7],[5,8,4]],1,2) # returns [[1,3],[5,8]]
print(result)
