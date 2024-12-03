"""
- Advent of code : 2024 -
-       Day 3           -
: Sas2k
"""
import re

puzzleInput = open("./day-3-input.txt", "r")

print("Advent Of Code 2024 - Day 3")

print("Part 1 Running....")
puzzle1Output = 0

puzzleInput = puzzleInput.read().replace("\n", "")

code = [i.replace("mul(", "").replace(")", "").split(",") for i in re.findall(r'mul\(\d{1,3},\d{1,3}\)', puzzleInput)]
for cur in code:
    puzzle1Output += int(cur[0]) * int(cur[1])

print(f"Part 1 Puzzle Output -> {puzzle1Output}")

print("Part 2 Running....")
puzzle2Output = 0
execute = True
Newcode = [i.replace("mul(", "").replace(")", "").split(",") if i[:3] == "mul" else i for i in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", puzzleInput)]
for Ncur in Newcode:
    if Ncur == "do()":
        execute = True
    elif Ncur == "don't()":
        execute = False
    elif execute:
        puzzle2Output += int(Ncur[0]) * int(Ncur[1])

print(f"Part 2 Puzzle Output -> {puzzle2Output}")
