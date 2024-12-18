"""
- Advent of Code 2024 -
-       Day 15        -
: Sas2k
"""

print("Advent of Code 2024 - Day 15")

puzzleInput = open("./day-15-input.txt", "r")
fileLen = sum(1 for _ in open("./day-15-input.txt"))

print("Formatting Data....")
warehouse = []
instructions = []

for y in range(0, fileLen):
    curLine = puzzleInput.readline()
    if curLine[0] == "#":
        row = []
        for x in range(0, len(curLine)):
            if curLine[x] == "@":
                bot = (x, y)
                row.append(".")
                continue
            elif curLine[x] == "\n":
                break
            row.append(curLine[x])
        warehouse.append(row)
    elif "v" in curLine:
        instructions = list(curLine.strip())
print("Data formatted")

print("----------")
print("\n".join([str(row) for row in warehouse]))

print("Part 1 Running....")
puzzle1Output = 0


def _Pushable(pos: list, dir: int, mapArr: list[list]) -> [bool, list]:
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    nextPos = [pos[0] + direction[dir][0], pos[1] + direction[dir][1]]

    if mapArr[nextPos[1]][nextPos[0]] == ".":
        return [True, pos]
    elif mapArr[nextPos[1]][nextPos[0]] == "#":
        return [False, pos]
    elif mapArr[nextPos[1]][nextPos[0]] == "O":
        return _Pushable(nextPos, dir, mapArr)


def PushBlock(pos: int, dir: int, mapArr: list[list]):
    check, nPos = _Pushable(pos, dir, mapArr)
    print(check, nPos)
    curPos = nPos
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    if check:
        delta = abs((nPos[0] - pos[0]) + (nPos[1] - pos[1]))
        for i in range(0, delta + 1):
            nextPos = [nPos[0] + direction[dir]
                       [0], nPos[1] + direction[dir][1]]
            mapArr[nextPos[1]][nextPos[0]] = mapArr[nPos[1]][nPos[0]]
            mapArr[nPos[1]][nPos[0]] = "."
            nPos = [nPos[0] - direction[dir][0], nPos[1] - direction[dir][1]]
            print(i, mapArr[nextPos[1]][nextPos[0]], mapArr[nPos[1]][nPos[0]])

        return curPos

    return pos


moves = ["^", ">", "v", "<"]
curX, curY = bot[0], bot[1]

for move in instructions:
    print("-------")
    curX, curY = PushBlock([curX, curY], moves.index(move), warehouse)
    print(move)
    print("\n".join([str(row) for row in warehouse]))
