"""
- Advent of code 2023 (post) -
-           Day 3            -
"""

puzzleInput = open("./day-3-input.txt")
fileLen = sum(1 for _ in open('./day-3-input.txt'))
#Processing data into a 2d array

print("Advent of Code 2023 (Post) - Day 3")
debug = input("Debug Mode[y/n]:>")

print("Formatting Data.....")
data = [["." for _ in range(len(puzzleInput.readline()) + 1)]]

puzzleInput.seek(0)

for i in range(0, fileLen):
    curline = puzzleInput.readline()
    row = ["."] + [i for i in curline[:-1]] + ["."]
    if debug == "y":
        print(row)
    data.append(row)

puzzleInput.seek(0)
data.append(["." for _ in range(len(puzzleInput.readline()) + 1)])
puzzleInput.close()

print("Complete.")

print("Part 1 Running....")

num = ""
puzzleOutput = 0
hasNeighbours = False

for y in range(1, len(data) - 1):
    for x in range(1, len(data[y]) - 1):
        neighbours = [data[y - 1][x - 1], data[y][x - 1], data[y + 1][x - 1],
                      data[y - 1][x], data[y + 1][x], data[y - 1][x + 1],
                      data[y][x + 1], data[y + 1][x + 1]] #Every Neighbour for a cell
        if data[y][x].isdigit():
            for n in range(0, len(neighbours)): # Yes, I know it sucks ( O(n^3) for worst time case....)
                if neighbours[n] != "." and not(neighbours[n].isdigit()):
                    hasNeighbours = True
            num += data[y][x]
            if x == len(data[y]) - 2 and y == len(data) - 2:
                if hasNeighbours == True:
                    hasNeighbours = False
                    puzzleOutput += int(num)
                    num = ""
        else:
            if hasNeighbours == True:
                hasNeighbours = False
                puzzleOutput += int(num)
                num = ""
            num = ""
        if debug == "y":
            print(data[y])
            print(neighbours, "\n", data[y][x], "\n", hasNeighbours, "\n", puzzleOutput)

print(f"Part 1 Puzzle Output -> {puzzleOutput}")
