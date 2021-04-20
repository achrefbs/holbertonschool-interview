#!/usr/bin/python3
"""
calculate how much water will be retained after it rains
"""


def rain(walls):
    """
    calculate how much water will be retained after it rains
    """
    sum = 0
    if not walls:
        return 0
    for i in range(1, len(walls) - 1):
        tmp = min(walls[i - 1], walls[i + 1])
        if (walls[i] < tmp):
            sum += tmp - walls[i]
    return sum
