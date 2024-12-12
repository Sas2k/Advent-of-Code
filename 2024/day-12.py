"""
- Advent of Code 2024 -
-        Day 12       -
: Sas2k
"""
import itertools

print("Advent of Code 2024 - Day 12")

puzzleInput = open("./day-12-input.txt", "r")
fileLen = sum(1 for _ in open("./day-12-input.txt"))

print("Formatting Data....")

data = []

for y in range(0, fileLen):
    curLine = puzzleInput.readline().strip()
    row = []
    for x in range(0, len(curLine)):
        row.append(curLine[x])
    data.append(row)

print("Done.")


def CheckNeighbours(x: int, y: int, mapArr: list[list[int]]) -> list:
    "Checks for every valid neighbour of a vegetable"
    cur = mapArr[y][x]
    neighbours = []
    yAdd = y + 1 < len(mapArr)
    xAdd = x + 1 < len(mapArr[y])
    ySub = y - 1 >= 0
    xSub = x - 1 >= 0

    if yAdd:
        neighbours.append((y + 1, x))
    if xSub:
        neighbours.append((y, x - 1))
    if xAdd:
        neighbours.append((y, x + 1))
    if ySub:
        neighbours.append((y - 1, x))

    perimeter = sum(1 for n in neighbours if mapArr[n[0]][n[1]] != cur) + sum(
        1 for conj in [yAdd, xAdd, ySub, xSub] if not conj)
    neighbours = [n for n in neighbours if mapArr[n[0]][n[1]] == cur]
    return neighbours, perimeter


def getSides(region: set, bound: tuple):
    corners = 0

    for y, x in itertools.product(range(-1, bound[0]), range(-1, bound[1])):
        tLeft = (y, x) in region
        bLeft = (y + 1, x) in region
        tRight = (y, x + 1) in region
        bRight = (y + 1, x + 1) in region

        gridSpaces = sum([tLeft, bLeft, tRight, bRight])
        corners += gridSpaces % 2

        if gridSpaces == 2 and ((tLeft and bRight) or (tRight and bLeft)):
            corners += 2

    return corners


def CalculatePrice(mapArr: list[list[int]], x: int, y: int) -> list:
    "Does a Depth First Search for vegetable patches and find it's price"
    visited = set()
    stack = [(y, x)]
    perimeter = 0

    while stack:
        cY, cX = stack.pop()
        if (cY, cX) not in visited:
            visited.add((cY, cX))
            neighbours, curPerimeter = CheckNeighbours(cX, cY, mapArr)

            for nY, nX in neighbours:
                stack.append((nY, nX))
            perimeter += curPerimeter

    return [len(set(visited)), perimeter, visited]


print("Part 1 & 2 Running....")
puzzle1Output = 0
puzzle2Output = 0

visited = set()

for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if (y, x) in visited:
            continue
        curInfo = CalculatePrice(data, x, y)
        puzzle1Output += curInfo[0] * curInfo[1]
        puzzle2Output += curInfo[0] * \
            getSides(curInfo[2], (len(data), len(data[0])))
        for coOrd in curInfo[2]:
            visited.add(coOrd)

print(f"Part 1 Puzzle Output -> {puzzle1Output}")
print(f"Part 2 Puzzle Output -> {puzzle2Output}")
