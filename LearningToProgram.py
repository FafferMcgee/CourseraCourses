# The design template for a function
"""
1. Examples
2. Type Contract
3. Header
4. Description
5. Body
6. Test
"""

# This is an example of a properly documented function


def perimeter(side1, side2, side3):

    """(number, number, number) -> number

    Returns the perimeter of a triangle with sides of length side1, side2, side3.

    >>> perimeter(3,4,5)
    12
    >>> perimeter(3.0,4.0,5)
    12.0
    """
    return side1 + side2 + side3

perimeter(3, 4, 5)

