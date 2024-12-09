"""
- Advent of code 2024 -
-        Day 8        -
: Sas2k
"""
from collections import defaultdict

print("Advent of code 2024 - Day 8")
debug = input("Debug Mode[y/n]:>")

puzzleInput = open("./day-8-input.txt", "r")
fileLen = fileLen = sum(1 for _ in open('./day-8-input.txt'))

print("Formatting data....")
data = []
coOrds = defaultdict(list[list])

for y in range(0, fileLen):
    curLine = puzzleInput.readline()
    row = []
    for x in range(0, len(curLine) - 1):
        if curLine[x] != ".":
            coOrds[curLine[x]].append([y, x])
        row.append(curLine[x])
    data.append(row)

print("Formatted.")

print("Running Part 1...")

antionant = set()

for antenna in list(coOrds.keys()):
    if len(coOrds[antenna]) == 1:
        continue
    TotSubsets = 1 << len(coOrds[antenna])
    for mask in range(0, TotSubsets):
        if bin(mask).count("1") == 2:
            sub = [0] * 2
            index = 0
            for i in range(0, len(coOrds[antenna])):
                if mask & (1 << i):
                    sub[index] = coOrds[antenna][i].copy()
                    index += 1
            if debug == "y":
                print(sub)

            xDif = sub[0][1] - sub[1][1]
            yDif = sub[0][0] - sub[1][0]
            p1 = [sub[1][1] - xDif if sub[1][1] - xDif >= 0 else len(data[0]) + 2,
                  sub[1][0] - yDif if sub[1][0] - yDif >= 0 else len(data[0]) + 2]
            p2 = [sub[0][1] + xDif if sub[0][1] + xDif >= 0 else len(data[0]) + 2,
                  sub[0][0] + yDif if sub[0][0] + yDif >= 0 else len(data[0]) + 2]

            try:
                if data[p1[1]][p1[0]] == "." or data[p1[1]][p1[0]] == "#":
                    data[p1[1]][p1[0]] = "#"
                else:
                    antionant.add(tuple(p1))
                print(p1, f"{antenna} at {sub}")
            except IndexError:
                pass
            try:
                if data[p2[1]][p2[0]] == "." or data[p2[1]][p2[0]] == "#":
                    data[p2[1]][p2[0]] = "#"
                else:
                    antionant.add(tuple(p2))
                print(p2, f"{antenna} at {sub}")
            except IndexError:
                pass

            if debug == "y":
                print(len(data))

print("".join(y + "\n" for y in ["".join(x) for x in data]))

puzzle1Output = "".join(["".join(x) for x in data]).count("#") + len(antionant)
print(f"Part 1 Puzzle Output -> {puzzle1Output}")
