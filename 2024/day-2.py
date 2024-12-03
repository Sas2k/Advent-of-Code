from collections import Counter

puzzleInput = open("./day-2-input.txt")
fileLen = sum(1 for _ in open('./day-2-input.txt'))

print("Advent of Code 2024: Day 2")
print("Length of Data: ", fileLen)

print("Part 1 Running....")
puzzle1Output = 0

for i in range(0, fileLen):
    curLine = puzzleInput.readline().split(" ")
    curLine = [int(curLine[num]) for num in range(0, len(curLine))]
    safe = True
    if all(curLine[i] < curLine[i + 1] for i in range(len(curLine) - 1)) or all(curLine[i] > curLine[i + 1] for i in range(len(curLine) - 1)):
        for n in range(0, len(curLine) - 1):
            if 3 < abs(curLine[n] - curLine[n + 1]) or curLine[n] == curLine[n + 1]:
                safe = False
                break
        if safe:
            puzzle1Output += 1

print(f"Puzzle Part 1 Output -> {puzzle1Output}")

print("Part 2 Running....")
puzzle2Output = 0

puzzleInput.seek(0)

for i in range(0, fileLen):
    curLine = puzzleInput.readline().split(" ")
    curLine = [int(curLine[num]) for num in range(0, len(curLine))]
    safe = True
    if all(curLine[i] < curLine[i + 1] for i in range(len(curLine) - 1)) or all(curLine[i] > curLine[i + 1] for i in range(len(curLine) - 1)):
        for n in range(0, len(curLine) - 1):
            if 3 < abs(curLine[n] - curLine[n + 1]) or curLine[n] == curLine[n + 1]:
                safe = False
                break
        if safe:
            puzzle2Output += 1
    if safe == False:
        sorts = curLine.copy()
        sorts.sort()
        count = 0
        if any(num <= 2 for num in Counter(curLine).values()):
            safe = True
        for j in range(0, len(curLine)):
            if sorts[j] != curLine[j]:
                count += 1
            elif count > 1:
                break
        if safe:
            puzzle2Output += 1
print(f"Puzzle Part 2 Output -> {puzzle2Output}")
