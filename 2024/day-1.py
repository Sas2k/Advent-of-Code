"""
-----------------------
- Advent of Code 2024 -
-      Day 1          -
-----------------------
: Sas2k
"""

puzzleInput = open("./day-1-input.txt", "r")
fileLen = sum(1 for _ in open('./day-1-input.txt'))

print("Advent of Code 2024: Day 1")

#Format the data into 2 lists
print("Formatting Data....")

dataA = []
dataB = []

for n in range(0, fileLen):
    curLine = puzzleInput.readline()
    dataA.append(int(curLine.split("   ")[0]))
    dataB.append(int(curLine.split("   ")[1]))

dataA.sort()
dataB.sort()

puzzleInput.seek(0)
puzzleInput.close()
print("Complete")

print("Part 1 Running....")

puzzle1Output = 0

for i in range(0, len(dataA)):
    puzzle1Output += abs(dataA[i] - dataB[i])

print(f"Part 1 Puzzle Output -> {puzzle1Output}")

print("Part 2 Running....")

puzzle2Output = 0

for i in range(0, len(dataB)):
    puzzle2Output += dataB.count(dataA[i]) * dataA[i]

print(f"Part 2 Puzzle Output -> {puzzle2Output}")
