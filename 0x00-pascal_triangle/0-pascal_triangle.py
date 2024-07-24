#!/usr/bin/python3
import math
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    
    triangle = []
    for row in range(n):
        rowlist = [1]
        for k in range(1, row):
            factN = math.factorial(row)
            factK = math.factorial(k)
            factDiff = math.factorial(row - k)
            result = factN // (factK * factDiff)
            rowlist.append(result)
        if row >= 1:
            rowlist.append(1)
        triangle.append(rowlist)
    return triangle
