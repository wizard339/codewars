"""
Given an array `arr` of strings complete the function `landPerimeter`
by calculating the total perimeter of all the islands. Each piece of
land will be marked with 'X' while the water fields are represented
as 'O'. Consider each tile being a perfect 1 x 1piece of land.

Some examples for better visualization:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']

 should return: "Total land perimeter: 24";

['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']

should return: "Total land perimeter: 18".
"""

import doctest


def land_perimeter(arr):
    """
    Tests:
    >>> land_perimeter(['XOOXO', 'XOOXO', 'OOOXO', 'XXOXO', 'OXOOO'])
    'Total land perimeter: 24'
    >>> land_perimeter(['XOOO', 'XOXO', 'XOXO', 'OOXX', 'OOOO'])
    'Total land perimeter: 18'
    """
    perimeter = 0
    for j in range(len(arr)):
        for k in range(len(arr[j])):
            if arr[j][k] == "X":
                perimeter += 4

                # check neighboring cells for equality to "X" if the neighboring
                # cell in a row or column is equal to "X" then the cell perimeter
                # is reduced by one

                if j != 0 and arr[j - 1][k] == "X":
                    perimeter -= 1
                if k != 0 and arr[j][k - 1] == "X":
                    perimeter -= 1
                if j != (len(arr) - 1) and arr[j + 1][k] == "X":
                    perimeter -= 1
                if k != (len(arr[j]) - 1) and arr[j][k + 1] == "X":
                    perimeter -= 1
    return f"Total land perimeter: {perimeter}"


if __name__ == '__main__':
    doctest.testmod(verbose=True)
