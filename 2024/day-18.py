"""
- Advent of Code 2024 -
-       Day 18        -
: Sas2k
"""
print("Advent of Code - Day 18")

puzzleInput = open("./day-18-input.txt", "r")
fileLen = sum(1 for _ in open("./day-18-input.txt"))

print("Formatting Data")
bytesData = []

memSpace = [["." for i in range(71)] for j in range(71)]

for column in range(0, fileLen):
    curLine = puzzleInput.readline()
    bytesData.append([int(row.strip()) for row in curLine.split(",")])

print("Formatted")

print("Part 1 Running")

for i in range(0, 1024):
    coOrd = bytesData[i]
    memSpace[coOrd[1]][coOrd[0]] = "#"


class DistanceGrid:
    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist


def check(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
        (y < len(grid) and x < len(grid[0])) and
            (grid[y][x] != '#') and (visited[y][x] is False)):
        return True
    return False


def bfs(maze: list[list], start: tuple, end: tuple):
    source = DistanceGrid(start[0], start[1], 0)

    visited = [[False for _ in range(len(maze[0]))]
               for _ in range(len(maze))]

    queue = []
    queue.append(source)
    visited[source.col][source.row] = True

    while len(queue) != 0:
        source = queue.pop(0)

        if (source.row, source.col) == end:
            return source.dist

        if check(source.row, source.col - 1, maze, visited):
            queue.append(DistanceGrid(source.row, source.col -
                         1, source.dist + 1))
            visited[source.col - 1][source.row] = True

        if check(source.row, source.col + 1, maze, visited):
            queue.append(DistanceGrid(source.row, source.col +
                         1, source.dist + 1))
            visited[source.col + 1][source.row] = True

        if check(source.row + 1, source.col, maze, visited):
            queue.append(DistanceGrid(source.row + 1, source.col,
                         source.dist + 1))
            visited[source.col][source.row + 1] = True

        if check(source.row - 1, source.col, maze, visited):
            queue.append(DistanceGrid(source.row - 1, source.col,
                         source.dist + 1))
            visited[source.col][source.row - 1] = True

    return -1


puzzle1Output = bfs(memSpace, (0, 0), (70, 70))

print(f"Part 1 Puzzle Output -> {puzzle1Output}")

print("Part 2 Running....")
puzzle2Output = list()

path = True
pointer = 1023

while path and pointer < fileLen:
    pointer += 1
    memSpace[bytesData[pointer][1]][bytesData[pointer][0]] = "#"
    path = bfs(memSpace, (0, 0), (70, 70)) != -1

puzzle2Output = bytesData[pointer]

print(f"Part 2 Puzzle Output -> {puzzle2Output}")
