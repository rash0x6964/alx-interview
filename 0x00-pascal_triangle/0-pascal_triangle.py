#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    """returns a list of lists of integers
        representing the Pascal’s triangle
    """

    if n <= 0:
        return []

    list = [[1]]

    for i in range(1, n):
        prev_row = list[-1]
        row = [1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)
        list.append(row)

    return list
