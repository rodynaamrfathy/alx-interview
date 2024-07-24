#!/usr/bin/python3
import math
"""pascal triangle function that returns a list of lists of integers representing the Pascal’s triangle of n"""

def pascal_triangle(n):
    if n <= 0:
        return []
    
    triangle = []
    for row in range(n):
        rowlist = []
        for k in range(row + 1):
            factN = math.factorial(row)
            factK = math.factorial(k)
            factDiff = math.factorial(row - k)
            result = factN // (factK * factDiff)
            rowlist.append(result)
        triangle.append(rowlist)
    return triangle
