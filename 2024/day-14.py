"""
- Advent of code 2024 -
-      Day 14         -
: Sas2k
"""
import os

puzzleInput = open("./day-14-input.txt")
fileLen = sum(1 for _ in open("./day-14-input.txt", "r"))

print("Formatting Data....")
robots = {}

for i in range(0, fileLen):
    curLine = puzzleInput.readline().strip().split(" ")
    pos = [int(num) for num in curLine[0].replace("p=", "").split(",")]
    vel = [int(num) for num in curLine[1].replace("v=", "").split(",")]
    robots[i] = {
        "pos": pos,
        "vel": vel
    }

floorMap = [[0 for i in range(11)] for j in range(7)]

print("Formatting Done.")


def move(robot: dict, time: int, mapArr: list[list[int]]) -> tuple:
    "Moves the robot with it's velocity for t(ime) seconds"
    curX, curY = robot["pos"]
    delX, delY = robot["vel"]
    maxY = len(mapArr)
    maxX = len(mapArr[0])
    curX = (curX + delX * time) % maxX
    curY = (curY + delY * time) % maxY

    return curX, curY


def getQuadrantSafety(mapArr: list[list[int]]) -> list:
    "Return Quadrant Counts"
    midX, midY = len(mapArr[0]) // 2, len(mapArr) // 2
    q1 = sum([sum(row[:midX]) for row in mapArr[:midY]])
    q2 = sum([sum(row[midX + 1:]) for row in mapArr[:midY]])
    q3 = sum([sum(row[:midX]) for row in mapArr[midY + 1:]])
    q4 = sum([sum(row[midX + 1:]) for row in mapArr[midY + 1:]])

    return q1 * q2 * q3 * q4


for i in range(0, fileLen):
    x, y = move(robots[i], 100, floorMap)
    floorMap[y][x] += 1

print("\n".join(["".join([str(num) if num != 0 else "." for num in floorMap[row]])
                 for row in range(0, len(floorMap))]))

print(f"Part 1 Output -> {getQuadrantSafety(floorMap)}")

deltaTime = 0  # 8100 <- Arbitary Value which worked on Puzzle Input I got.

while True:
    updateMap = [[0 for i in range(11)] for j in range(7)]
    deltaTime += 1
    for i in range(0, fileLen):
        x, y = move(robots[i], deltaTime, updateMap)
        updateMap[y][x] = "#"

    print("\n".join(["".join([str(num) if num == "#" else "_" for num in updateMap[row]])
                     for row in range(0, len(updateMap))]))

    print(f"Time -> {deltaTime}")
    stop = input("Stop?[y/n]:>") == "y"
    if stop:
        break
    os.system("cls")

print(f"Part 2 Output -> {deltaTime}")
