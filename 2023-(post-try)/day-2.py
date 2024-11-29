"""
- Advent of code 2023 (post) -
-          Day 2             -
"""

puzzleInput = open("./day-2-input.txt", "r")
fileLen = sum(1 for _ in open('./day-2-input.txt'))

print("Advent of code 2023: Day 2")

debug = input("Run debug mode(y/n):]")

print("Formatting data to be used....")
#format the data into a dictionary
data = {}

for i in range(0, fileLen):
    #Game x: a red, b blue; c green, d red
    curline = puzzleInput.readline()
    gameID = int(curline.split(":")[0].replace("Game ", ""))
    body = curline.split(":")[1].replace(";", ",").replace("\n", "").split(",")
    data[gameID] = {
        "red": 0,
        "blue": 0,
        "green": 0
    }
    if debug == "y":
        print(gameID, body)
    for j in range(0, len(body)):
        instance = body[j].strip()
        if debug == "y":
            print(instance)
        if instance.split(" ")[1] == "red":
            data[gameID]["red"] = max(int(instance.split(" ")[0]), data[gameID]["red"])
        elif instance.split(" ")[1] == "blue":
            data[gameID]["blue"] = max(int(instance.split(" ")[0]), data[gameID]["blue"])
        else:
            data[gameID]["green"] = max(int(instance.split(" ")[0]), data[gameID]["green"])

if debug == "y":
    print(data)

print("Part 1 running....")

puzzleOutput = 0

for k in range(0, len(data)):
    cur = data[k + 1]
    if cur["red"] <= 12 and cur["blue"] <= 14 and cur["green"] <= 13:
        puzzleOutput += k + 1
        if debug == "y":
            print(k + 1)

print("Part 1 Output -> ", puzzleOutput)

print("Part 2 running....")

puzzleOutput2 = 0

for l in range(0, len(data)):
    curProduct = data[l + 1]["red"] * data[l + 1]["blue"] * data[l + 1]["green"] #Generating the power of the set
    if debug == "y":
        print(f'{curProduct} -> {data[l + 1]["red"]} * {data[l + 1]["blue"]} * {data[l + 1]["green"]}')
    puzzleOutput2 += curProduct

print("Part 2 Output -> ", puzzleOutput2)
