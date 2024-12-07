"""
- Advent of code 2024 -
-        Day 7        -
: Sas2k
"""

print("Advent of code 2024 - Day 7")

debug = input("Debug Mode[y/n]:>")

print("Formatting Data....")

puzzleInput = open("./day-7-input.txt", "r")
fileLen = fileLen = sum(1 for _ in open('./day-7-input.txt'))

data = []

for i in range(0, fileLen):
    curLine = puzzleInput.readline()
    values = [int(num) for num in curLine.split(": ")[1].split(" ")]
    target = int(curLine.split(": ")[0])
    data.append([target, values])

print("Data formatted.")

print("Part 1 running....")
puzzle1Output = 0

for key in data:  # <- Loads in the test cases
    if debug == "y":
        print(key)
    for n in range(0, 2**len(key[1])):
        pattern = str(bin(n))[2:].zfill(len(key[1]))
        curSum = 0
        if debug == "y":
            print(pattern, key)
        for i in range(0, len(pattern)):
            if pattern[i] == "0":
                curSum += key[1][i]
            else:
                curSum *= key[1][i]
        if curSum == key[0]:
            puzzle1Output += key[0]
            break

print(f"Part 1 Puzzle Output -> {puzzle1Output}")

print("Part 2 running....")
puzzle2Output = 0


def ternary(n: int) -> str:
    "Converts decimal to ternary"
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))


debug = input("Continue[y/n]")

for key in data:  # <- Loads in the test cases
    if debug == "y":
        print(key)
    for n in range(0, 3**len(key[1])):
        pattern = str(ternary(n)).zfill(len(key[1]))
        curSum = 0
        if debug == "y":
            print(n)
            print(pattern, key)
        for i in range(0, len(pattern)):
            if pattern[i] == "0":
                curSum += key[1][i]
            elif pattern[i] == "1":
                curSum *= key[1][i]
            else:
                curSum = int(f"{curSum}{key[1][i]}")
        if curSum == key[0]:
            puzzle2Output += key[0]
            break

print(f"Part 2 Puzzle Output -> {puzzle2Output}")
