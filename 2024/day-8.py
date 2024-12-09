"""
- Advent of code 2024 -
-        Day 8        -
: Sas2k
"""
from collections import defaultdict

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


data = OgData.copy()
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
data = OgData.copy()

print(data)


def NextSuccesivePoints(p1, p2, points):
    "Gets every points within the boundry which is created by the 2 points"
    xDif = p1[1] - p2[1]
    yDif = p1[0] - p2[0]

    print(p1, p2)
    cur = p1

    while 0 <= cur[0] < len(data) - 1 and 0 <= cur[1] < len(data[0]) - 1:
        cur = (cur[0] + yDif, cur[1] + xDif)
        points.add(cur)
        print(cur)

    cur = p2

    while 0 <= cur[0] < len(data) - 1 and 0 <= cur[1] < len(data[0]) - 1:
        cur = (cur[0] - yDif, cur[1] - xDif)
        points.add(cur)
        print(cur)


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

            points = set()
            NextSuccesivePoints(sub[0], sub[1], points)
            print(points)
            for point in points:
                PlaceAntinode(point, data, visitedAnt2)

if debug == "y":
    print("".join(y + "\n" for y in ["".join(x) for x in data]))

puzzle2Output = "".join(["".join(x)
                        for x in data]).count("#") + len(visitedAnt2)
print(f"Part 2 Puzzle Output -> {puzzle2Output}")
