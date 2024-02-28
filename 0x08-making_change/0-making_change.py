#!/usr/bin/python3

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
    if total == 0 or len(coins) == 0:
        return 0
    coins = bubbleSort(coins)
    print(coins)
    result = 0
    for coin in coins:
        if coin == 0:
            continue
        while total >= coin:
            total -= coin
            result += 1

    return result if total == 0 else -1
