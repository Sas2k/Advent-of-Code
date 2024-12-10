"""
- Advent of code 2024 -
-       Day 9         -
: Sas2k
"""
from progress.bar import ShadyBar

print("Advent of code 2024 - Day 9")
debug = input("Debug Statements?[y/n]:>")

puzzleInput = open("./day-9-input.txt", "r").read().replace("\n", "")

print("Part 1 Running....")

disk = ""
puzzle1Output = 0

if debug == "n":
    bar = ShadyBar("Formatting:", max=len(puzzleInput)//2)

for n in range(0, len(puzzleInput), 2):
    if debug == "y":
        print(n, puzzleInput[n])
    disk = f"{disk}{"".join(["|"+str(n//2)]*int(puzzleInput[n]))}"
    if n + 1 < len(puzzleInput):
        disk = f"{disk}{"".join(["|."]*int(puzzleInput[n+1]))}"
    if debug == "n":
        bar.next()

if debug == "y":
    print(disk)

# Formatting Disk
disk = disk.split("|")

if debug == "n":
    bar2 = ShadyBar("Calculating:", max=disk.count("."))

for i in range(len(disk) - 1, -1, -1):
    free = len(disk) - i
    if debug == "y":
        print(i)
    if free > disk.count("."):
        break
    if disk[i] == ".":
        continue
    char = disk[i]
    disk[i] = "."
    disk[disk.index(".", free)] = char
    if debug == "n":
        bar2.next()

if debug == "y":
    print("".join(disk))

if debug == "n":
    bar3 = ShadyBar("Finalizing:", max=disk.index("."))

for i in range(1, disk.index(".")):
    if debug == "y":
        print(int(disk[i]), i)
    puzzle1Output += (i-1) * int(disk[i])
    if debug == "n":
        bar3.next()

print(f"Part 1 Puzzle Output -> {puzzle1Output}")

print("Part 2 Running....")
puzzle2Output = 0

clumpedDisk = []
freeSpaces = []

for n in range(0, len(puzzleInput), 2):
    clumpedDisk.append([str(n // 2)] * int(puzzleInput[n]))
    if n + 1 < len(puzzleInput):
        if int(puzzleInput[n + 1]) >= 1:
            clumpedDisk.append(["."] * int(puzzleInput[n + 1]))
            freeSpaces.append(n + 1)

if debug == "y":
    print(clumpedDisk)
else:
    bar4 = ShadyBar("Fragmenting Disk:", max=len(clumpedDisk))

for j in reversed(range(len(clumpedDisk))):
    if clumpedDisk[j].count(".") == len(clumpedDisk[j]):
        if debug == "n":
            bar4.next()
        continue
    cur = j
    k = 0
    while k < len(freeSpaces):
        space = freeSpaces[k]
        if clumpedDisk[space].count(".") >= len(clumpedDisk[cur]):
            if clumpedDisk[space].count(".") <= 0:
                k += 1
                continue
            elif clumpedDisk[space].count(".") == 1:
                clumpedDisk[space][clumpedDisk[space].index(
                    ".")] = clumpedDisk[cur][0]
                clumpedDisk[cur][0] = '.'
                k += 1
                continue
            for i in range(0, len(clumpedDisk[cur])):
                if clumpedDisk[space][i] == ".":
                    clumpedDisk[space][i] = clumpedDisk[cur][i]
            clumpedDisk[cur] = ["."]*len(clumpedDisk[cur])
            break
        k += 1
    if debug == "n":
        bar4.next()

if debug == "y":
    print(f"Fragmented disk :> {clumpedDisk}")

if clumpedDisk[0].count(".") == len(clumpedDisk[0]):
    clumpedDisk = clumpedDisk[1:]

print(clumpedDisk)
id = 0

for y in range(0, len(clumpedDisk)):
    for x in range(0, len(clumpedDisk[y])):
        if clumpedDisk[y][x] == ".":
            id += 1
            continue
        puzzle2Output += id * int(clumpedDisk[y][x])
        id += 1

print(f"Part 2 Puzzle Output -> {puzzle2Output}")
