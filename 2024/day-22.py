"""
- Advent of Code 2024 -
-       Day 22        -
: Sas2k
"""
from functools import cache

print("Advent of Code 2024 - Day 22")

puzzleInput = open("./day-22-input.txt", "r")
nums = [int(string.strip()) for string in puzzleInput.readlines()]
puzzleInput.close()

print("Part 1 Running....")


@cache
def mix(secret: int, num: int) -> int:
    "Mixes the number"
    return num ^ secret


@cache
def prune(secret: int) -> int:
    "Prunes the number"
    return secret % 16777216


puzzle1Output = []

for num in nums:
    secret = num
    for i in range(0, 2000):
        secret = prune(mix(secret, secret * 64))
        secret = prune(mix(secret, secret // 32))
        secret = prune(mix(secret, secret * 2048))
    puzzle1Output.append(secret)

print(f"Part 1 Puzzle Output -> {sum(puzzle1Output)}")
