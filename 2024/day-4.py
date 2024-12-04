"""
- Advent of Code 2024 -
-       Day 4         -
: Sas2k
"""
import re
from collections import defaultdict

puzzleInput = open("./day-4-input.txt", "r")
fileLen = fileLen = sum(1 for _ in open('./day-4-input.txt'))

print("Advent of Code 2024 - Day 4")

debug = input("Debug statements[y/n]:>")

print("Formatting Data...")

data = []

for line in range(0, fileLen):
    curLine = puzzleInput.readline().replace("\n", "")
    data.append([char for char in curLine])

puzzleInput.close()
print("Done...")

def groups(data, func):
    "gets the relevant items from the conditions given by func from data"
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

print("Part 1 Running....")
word = "XMAS"
puzzle1Output = 0

dataH = data.copy()
dataH = list(zip(*dataH))
dataLR = groups(data, lambda x, y: x + y)
dataRR = groups(data, lambda x, y: x - y)

for cLine in data: #Horizontal
    cLine = "".join(cLine)
    puzzle1Output += len(re.findall(fr'(?=({word}|{word[::-1]}))', cLine))

for cLine in dataH: #Vertical
    cLine = "".join(cLine)
    puzzle1Output += len(re.findall(fr'(?=({word}|{word[::-1]}))', cLine))
    if debug == "y":
        print(cLine)
        
for cLine in dataLR: #Diagonal
    cLine = "".join(cLine)
    puzzle1Output += len(re.findall(fr'(?=({word}|{word[::-1]}))', cLine))
    if debug == "y":
        print(cLine)

for cLine in dataRR: #Diagonal
    cLine = "".join(cLine)
    puzzle1Output += len(re.findall(fr'(?=({word}|{word[::-1]}))', cLine))
    if debug == "y":
        print(cLine)

print(f"Part 1 Puzzle Output -> {puzzle1Output}")

print("Part 2 Running....")
puzzle2Output = 0

for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x] == "A":
            rD = "A"
            lD = "A"
            if y - 1 >= 0 and x - 1 >= 0:
                rD = data[y-1][x-1] + rD
            if y + 1 < len(data) and x + 1 < len(data[y]):
                rD = rD + data[y+1][x+1]
            if y + 1 < len(data) and x - 1 >= 0:
                lD = data[y+1][x-1] + lD
            if y - 1 >= 0 and x + 1 < len(data[y]):
                lD = lD + data[y-1][x+1]
            if rD in ["MAS", "SAM"] and lD in ["MAS", "SAM"]:
                puzzle2Output += 1
                
print(f"Part 2 Puzzle Output -> {puzzle2Output}")
