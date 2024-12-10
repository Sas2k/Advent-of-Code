"""
- Advent of code 2024 -
-       Day 10        -
: Sas2k
"""
from rich.console import Console
import os

print("Advent of code 2024 - Day 10")
debug = input("Debug statements[y/n]:>")

console = Console()

puzzleInput = open("./day-10-input.txt", "r")
fileLen = sum(1 for _ in open("./day-10-input.txt"))

print('Formatting Data....')
Map = []
Headers = []

for y in range(0, fileLen):
    curLine = puzzleInput.readline().replace("\n", "")
    row = []
    for x in range(0, len(curLine)):
        if curLine[x] == "0":
            Headers.append([y, x])
        row.append(int(curLine[x]))
    Map.append(row)


def ShowMap(mapArr: list[list[int]], px: int, py: int, visited: list):
    "Shows the current map"
    for y in range(0, len(mapArr)):
        row = ""
        for x in range(0, len(mapArr[y])):
            if px == x and py == y:
                row += f"[red]{mapArr[y][x]}[/red]"
                continue
            if (y, x) in visited:
                row += f"[yellow]{mapArr[y][x]}[/yellow]"
            else:
                row += str(mapArr[y][x])
        console.print(row)


if debug == "y":
    print(Headers)
print("Done.")

print("Running Part 1")


def CheckNeighbours(x: int, y: int, mapArr: list[list[int]]) -> list:
    "Checks for every valid neighbour of a point"
    cur = mapArr[y][x]
    neighbours = []
    yAdd = y + 1 < len(mapArr)
    xAdd = x + 1 < len(mapArr[y])
    ySub = y - 1 >= 0
    xSub = x - 1 >= 0

    if yAdd and cur + 1 == mapArr[y + 1][x]:
        neighbours.append((y + 1, x))
    if xSub and cur + 1 == mapArr[y][x - 1]:
        neighbours.append((y, x - 1))
    if xAdd and cur + 1 == mapArr[y][x + 1]:
        neighbours.append((y, x + 1))
    if ySub and cur + 1 == mapArr[y - 1][x]:
        neighbours.append((y - 1, x))

    return neighbours


def dfs(mapArr: list[list[int]], x: int, y: int):
    "Depth first search"

    visited = set()
    stack = [(y, x)]
    nines = set()

    while stack:
        cY, cX = stack.pop()
        if (cY, cX) not in visited:
            if 0 > cY or 0 > cX:
                continue
            visited.add((cY, cX))
            neighbours = CheckNeighbours(cX, cY, mapArr)

            if debug == "y":
                print(f"Pos: {x} {y} -> {neighbours}")
                ShowMap(mapArr, x, y, list(visited))
                os.system("cls")

            for nY, nX in neighbours:
                if mapArr[nY][nX] == 9:
                    nines.add((nY, nX))

                stack.append((nY, nX))

    print(visited)
    return len(nines)


curMap = Map.copy()
puzzle1Output = 0

for i in range(0, len(Headers)):
    Y = Headers[i][0]
    X = Headers[i][1]

    puzzle1Output += dfs(curMap, X, Y)

print(f"Part 1 Puzzle Output -> {puzzle1Output}")
