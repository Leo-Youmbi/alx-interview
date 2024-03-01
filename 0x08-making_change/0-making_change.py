#!/usr/bin/python3
"""Change making module.
"""


from typing import List


def bubbleSort(li: List[int]) -> List[int]:
    """Bubble sorts a list of integers"""
    newList = li.copy()
    size = len(newList)
    for i in range(size):
        for j in range(size-i-1):
            if newList[j] < newList[j+1]:
                newList[j], newList[j+1] = newList[j+1], newList[j]
    return newList


def makeChange(coins: List[int], total: int) -> int:
    """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    # coins = bubbleSort(coins)
    coins = sorted(coins, reverse=True)
    result = 0
    for coin in coins:
        if total == 0 or coin == 0:
            break
        while total >= coin:
            total -= coin
            result += 1

    return result if total == 0 else -1
