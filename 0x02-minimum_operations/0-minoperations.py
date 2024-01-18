#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if n < 2:
        return 0

    maxi_divs = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            maxi_divs = max(maxi_divs, i, n//i)

    if maxi_divs == 1:
        return n

    return minOperations(maxi_divs) + n//maxi_divs
