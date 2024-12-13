"""
- Advent of Code 2024 -
-        Day 13       -
: Sas2k
"""
from collections import defaultdict
from sympy import Eq, solve
from sympy.abc import a, b, c, d

print("Advent of Code 2024 - Day 13")

puzzleInput = open("./day-13-input.txt")
fileLen = sum(1 for _ in open("./day-13-input.txt"))

data = defaultdict(dict)
line = 0
for i in range(0, fileLen):
    curLine = puzzleInput.readline().replace("\n", "")

    if len(curLine) == 0:
        line += 1
    elif curLine[0:10] == "Button A: ":
        nums = curLine[10:].split(", ")
        data[line]["A"] = ((int(nums[0].replace("X+", "")),
                           int(nums[1].replace("Y+", ""))))
    elif curLine[0:10] == "Button B: ":
        nums = curLine[10:].split(", ")
        data[line]["B"] = ((int(nums[0].replace("X+", "")),
                           int(nums[1].replace("Y+", ""))))
    elif curLine[0:7] == "Prize: ":
        nums = curLine[7:].split(", ")
        data[line]["Prize"] = ((int(nums[0].replace("X=", "")),
                                int(nums[1].replace("Y=", ""))))

print("Formatting done.")

print("Part 1 & 2 Running....")
puzzle1Output = 0
puzzle2Output = 0

for n in range(0, line + 1):
    x1, y1 = data[n]["A"][0], data[n]["A"][1]
    x2, y2 = data[n]["B"][0], data[n]["B"][1]
    xC, yC = data[n]["Prize"][0], data[n]["Prize"][1]
    xD, yD = xC + 10000000000000, yC + 10000000000000

    solved = solve([
        Eq(a*x1 + b*x2, xC),
        Eq(a*y1 + b*y2, yC)
    ])

    solved2 = solve([
        Eq(c*x1 + d*x2, xD),
        Eq(c*y1 + d*y2, yD)
    ])

    tokenA = {s: solved[s].evalf() for s in solved}[a]
    tokenB = {s: solved[s].evalf() for s in solved}[b]
    tokenC = {s: solved2[s].evalf() for s in solved2}[c]
    tokenD = {s: solved2[s].evalf() for s in solved2}[d]

    if float(int(tokenA)) == tokenA and float(int(tokenB)) == tokenB:
        puzzle1Output += tokenA * 3 + tokenB
    if float(int(tokenC)) == tokenC and float(int(tokenD)) == tokenD:
        puzzle2Output += tokenC * 3 + tokenD

print(f"Part 1 Puzzle Output -> {int(puzzle1Output)}")
print(f"Part 2 Puzzle Output -> {int(puzzle2Output)}")
