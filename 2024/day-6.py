"""
- Advent of code 2024 -
-       Day 6         -
: Sas2k
"""
import os
import time
import copy

print("Advent of code 2024 - Day 6")

puzzleInput = open("./day-6-input.txt", "r")
fileLen = sum(1 for _ in open('./day-6-input.txt'))

print("Formatting Data....")
data = [["|" for i in range(0, (len(puzzleInput.readlines()[0]) + 1))]]
puzzleInput.seek(0)

for y in range(0, fileLen):
    curLine = puzzleInput.readline().replace("\n", "")
    curLine = ["|"] + [cur for cur in curLine] + ["|"]

    if "^" in curLine:
        startX = curLine.index("^")
        startY = y + 1

    data.append(curLine)

puzzleInput.seek(0)
data.append(["|"] * (len(puzzleInput.readlines()[0]) + 1))

puzzleInput.close()
print("Finished.")

print("Part 1 Running....")
direction = 0

curX, curY = startX, startY
maze = copy.deepcopy(data)


def showBoard(arr: list[list[str]]) -> str:
    "Shows the board as a string"
    board = "".join("".join(line + ["\n"]) for line in arr)
    return board


while maze[curY][curX] != "|":
    maze[curY][curX] = "X"
    x, y = curX, curY
    if direction == 0:
        curY -= 1
    elif direction == 1:
        curX += 1
    elif direction == 2:
        curY += 1
    else:
        curX -= 1
    if maze[curY][curX] == "#":
        curX = x
        curY = y
        direction = direction + 1 if direction < 4 else 0

print(f"Final Board: \n{showBoard(maze)}")

puzzle1Output = showBoard(maze).count("X")

print("Part 1 Puzzle Output -> ", puzzle1Output)

print("Part 2 Running....")
puzzle2Output = 0
curX, curY = startX, startY

for y in range(1, len(data) - 1):
    for x in range(1, len(data[y]) - 1):
        if maze[y][x] == "X" and [x, y] != [startX, startY]:
            temps = data[y][x]
            data[y][x] = "O"
        else:
            continue
        curX, curY = startX, startY
        i = 0
        while data[curY][curX] != "|":
            # print("obj: ", y, x)
            # print(curX, curY)
            # temp = data[curX][curY]
            # data[curY][curX] = "^"
            # print(showBoard(data))
            # data[curY][curX] = temp
            # time.sleep(0.1)
            # os.system("cls")
            pX, pY = curX, curY
            if direction == 0:
                curY -= 1
            elif direction == 1:
                curX += 1
            elif direction == 2:
                curY += 1
            else:
                curX -= 1
            if data[curY][curX] == "#" or data[curY][curX] == "O":
                curX = pX
                curY = pY
                direction = direction + 1 if direction < 4 else 0
            if curY == startY and curX == startX and i > 0:
                puzzle2Output += 1
                # print("Cycle!, ", puzzle2Output)
                break
            print(y, x, i, curX, curY, puzzle2Output)
            i += 1
        # print(showBoard(data))
        # time.sleep(0.5)
        # os.system("cls")
        data[y][x] = temps

print("Part 2 Puzzle Output -> ", puzzle2Output)
