"""
- Advent of Code 2024 -
-       Day 16        -
: Sas2k
"""
import os
import time

print("Advent of Code 2024 - Day 16")

puzzleInput = open("./day-16-input.txt", "r")
fileLen = sum(1 for _ in open("./day-16-input.txt"))

print("Formatting Data....")
maze = []
start = ()
end = ()

for y in range(0, fileLen):
    curLine = puzzleInput.readline()
    row = []
    for x in range(0, len(curLine)):
        if curLine[x] == 'E':
            end = (x, y)
        elif curLine[x] == 'S':
            start = (x, y)
        row.append(curLine[x])
    maze.append(row)

print("Formatting done.")

print("Part 1 running....")
puzzle1Output = 0


def showBoard(board: list[list], pos: tuple):
    print("------")
    for y in range(0, len(board)):
        row = []
        for x in range(0, len(board[y])):
            if (y, x) == pos:
                row.append("P")
                continue
            row.append(board[y][x])
        print("".join(row))
    time.sleep(0.2)
    os.system("cls")


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


def get_turn_cost(current_dir, next_dir):
    """Calculates the turning cost based on the current and next directions."""
    if current_dir == next_dir:
        return 1
    elif (current_dir + 1) % 4 == next_dir:
        return 1001  # Clockwise turn
    elif (current_dir - 1) % 4 == next_dir:
        return 1001  # Anticlockwise turn
    else:
        return 2001


def bfs(maze: list[list], start: tuple, end: tuple):
    source = DistanceGrid(start[0], start[1], 0)

    visited = [[False for _ in range(len(maze[0]))]
               for _ in range(len(maze))]

    queue = []
    queue.append([2, source])
    visited[source.col][source.row] = True
    dir = 2  # East (counting clockwise)

    routes = []

    while len(queue) != 0:
        dir, source = queue.pop(0)

        maze[source.col][source.row] = ["<", "V", ">", "^"][dir]
        # showBoard(maze, (source.row, source.col))

        if (source.row, source.col) == end:
            routes.append(source.dist)
            visited[source.col][source.row] = False
            continue

        if check(source.row, source.col - 1, maze, visited):
            queue.append([3, DistanceGrid(source.row, source.col -
                         1, source.dist + get_turn_cost(dir, 3))])
            visited[source.col - 1][source.row] = True
            dir = 3

        if check(source.row, source.col + 1, maze, visited):
            queue.append([1, DistanceGrid(source.row, source.col +
                         1, source.dist + get_turn_cost(dir, 1))])
            visited[source.col + 1][source.row] = True
            dir = 1

        if check(source.row + 1, source.col, maze, visited):
            queue.append([2, DistanceGrid(source.row + 1, source.col,
                         source.dist + get_turn_cost(dir, 2))])
            visited[source.col][source.row + 1] = True
            dir = 2

        if check(source.row - 1, source.col, maze, visited):
            queue.append([0, DistanceGrid(source.row - 1, source.col,
                         source.dist + get_turn_cost(dir, 0))])
            visited[source.col][source.row - 1] = True
            dir = 0

    return routes


print(f"Part 1 Puzzle Output -> {min(bfs(maze, start, end))}")
