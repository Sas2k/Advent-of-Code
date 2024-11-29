"""
- Advent of code 2023 (post) -
-           Day 3            -
"""

puzzleInput = open("./day-3-input.txt")
fileLen = sum(1 for _ in open('./day-3-input.txt'))
#Processing data into a 2d array

data = [0 for l in range(0, len(puzzleInput.readlines()[0])) - 1]

for i in range(0, fileLen):
    curline = puzzleInput.readline()
    row = [0] + [i for i in curline[:-1]] + [0]
    # print(row)
    data.append(row)

data.append([0 for l in range(0, len(puzzleInput.readlines()[0]) - 1)])

print(data)

"""
for y in range(0, len(data)):
    for x in range(0, len(data[y])):
        if data[y][x].isdigit():
"""
