"""
- Advent of Code 2024 -
-       Day 11        -
: Sas2k
"""
import textwrap

from functools import cache

print("Advent of Code 2024 - Day 11")
debug = input("Debug Mode[y/n]:>")

puzzleInput = open("./day-11-input.txt", "r")
stones = puzzleInput.readline().split(" ")

print("Part 1 & 2 Running....")

if debug == "y":
    print(stones)


@cache
def blink(n: int, stone: str) -> int:
    if debug == "y":
        print(n, stone)
    if n <= 0:
        return 1
    if int(stone) == 0:
        return blink(n - 1, 1)

    if len(str(stone)) % 2 == 0:
        div = len(stone) // 2
        return blink(n - 1, str(int(stone[:div]))) + blink(n - 1, str(int(stone[div:])))
    else:
        return blink(n - 1, str(int(stone) * 2024))


puzzle1Output = 0
puzzle2Output = 0

for stone in stones:
    puzzle1Output += blink(25, stone.strip())

print(f"Part 1 puzzle output -> {puzzle1Output}")

for stone in stones:
    puzzle2Output += blink(75, stone.strip())

print(f"Part 2 puzzle output -> {puzzle2Output}")
