"""
- Advent of code 2024 -
-        Day 8        -
: Sas2k
"""
from collections import defaultdict
from copy import copy
from itertools import combinations

print("Advent of code 2024 - Day 8")
debug = input("Debug Mode[y/n]:>")

puzzleInput = open("./day-8-input.txt", "r")
fileLen = fileLen = sum(1 for _ in open('./day-8-input.txt'))

print("Formatting data....")
OgData = []
coOrds = defaultdict(list[tuple])

for y in range(0, fileLen):
    curLine = puzzleInput.readline()
    row = []
    for x in range(0, len(curLine) - 1):
        if curLine[x] != ".":
            coOrds[curLine[x]].append((y, x))
        row.append(curLine[x])
    OgData.append(row)

if debug == "y":
    print(OgData, coOrds)

print("Formatted.")

print("Running Part 1...")


def NextPoints(point1: list, point2: list) -> list:
    "Returns two consecutive positions"
    xDif = point2[1] - point1[1]
    yDif = point2[0] - point1[0]
    np1 = [point1[0] - yDif if point1[0] - yDif >= 0 else len(
        data[0]) + 2, point1[1] - xDif if point1[1] - xDif >= 0 else len(data[0]) + 2]
    np2 = [point2[0] + yDif if point2[0] + yDif >= 0 else len(
        data[0]) + 2, point2[1] + xDif if point2[1] + xDif >= 0 else len(data[0]) + 2]
    return np1[::-1], np2[::-1]


def PlaceAntinode(location: list, data: list[list], visited: set[tuple]):
    "tries to place an antinode"
    try:
        if data[location[1]][location[0]] == "." or data[location[1]][location[0]] == "#":
            data[location[1]][location[0]] = "#"
        else:
            visited.add(tuple(location))
        print(location)
    except IndexError:
        return None


data = copy(OgData)
visitedAnt = set()

for antenna in coOrds.keys():
    if len(coOrds[antenna]) == 1:
        continue
    TotSubsets = 1 << len(coOrds[antenna])
    for mask in range(0, TotSubsets):
        if debug == "y":
            print(mask)
        if bin(mask).count("1") == 2:
            sub = [0] * 2
            index = 0
            for i in range(0, len(coOrds[antenna])):
                if mask & (1 << i):
                    sub[index] = coOrds[antenna][i]
                    index += 1

            p1, p2 = NextPoints(sub[0], sub[1])
            PlaceAntinode(p1, data, visitedAnt)
            PlaceAntinode(p2, data, visitedAnt)

if debug == "y":
    print("".join(y + "\n" for y in ["".join(x) for x in data]))

puzzle1Output = "".join(["".join(x)
                        for x in data]).count("#") + len(visitedAnt)
print(f"Part 1 Puzzle Output -> {puzzle1Output}")

print("Part 2 Running....")
puzzle2Output = 0

visitedAnt2 = set()
data2 = []

for row in OgData:
    row = [x.replace("#", ".") for x in row]
    data2.append(row)

print(data2)

if len(data2[-1]) < len(data2[0]):
    for i in range(0, abs(len(data2[0]) - len(data2[-1]))):
        data2[-1].append(".")


def NextSuccesivePoints(p1, p2):
    "Gets every points within the boundry which is created by the 2 points"
    distance = (p2[1] - p1[1], p2[0] - p1[0])
    x1, y1 = p1
    x2, y2 = p2
    points = set()
    for k in range(1, max(len(data), len(data[0]))):
        if x1 == x2:  # Same row
            antinode_one = (min(y1, y2) - k * distance[1], x1)
            antinode_two = (max(y1, y2) + k * distance[1], x1)
        elif y1 == y2:  # Same column
            antinode_one = (y1, min(x1, x2) - k * distance[0])
            antinode_two = (y1, max(x1, x2) + k * distance[0])
        else:  # Diagonal
            antinode_one = (y1 - k * distance[1], x1 - k * distance[0])
            antinode_two = (y2 + k * distance[1], x2 - k * distance[0])
        if 0 <= antinode_one[0] < len(data2) and 0 <= antinode_one[1] < len(data2[0]):
            points.add(antinode_one)
        if 0 <= antinode_two[0] < len(data2) and 0 <= antinode_two[1] < len(data2[0]):
            points.add(antinode_two)

    for point in points:
        PlaceAntinode(list(point), visitedAnt2, data2)


for antenna in coOrds.keys():
    if len(coOrds[antenna]) == 1:
        continue
    for p1, p2 in list(combinations(coOrds[antenna], 2)):
        NextSuccesivePoints(p1, p2)

if debug == "y":
    print("".join(y + "\n" for y in ["".join(x) for x in data2]))

puzzle2Output = "".join(["".join(x)
                        for x in data2]).count("#") + len(visitedAnt2)
print(f"Part 2 Puzzle Output -> {puzzle2Output}")
