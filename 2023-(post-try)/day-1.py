"""
- Advent of code 2023 (post) -
  Day 1
"""
import re

puzzleText = open("./day-1-input.txt", "r")

puzzleOutput = 0

print("Advent of code: 2023 - Day 1 Running -")

debug = input("Do you want the debug statesments to show? [y/n]:>")

print("Part 1:")

for i in range(0, 1000):
    curline = re.sub(r"\D", "", puzzleText.readline()) #Just gets all of the numeric characters
    cursum = int(curline[0] + curline[-1])
    puzzleOutput += cursum
    if debug == "y":
        print(f"{i} : {curline} ({cursum}) -> {puzzleOutput}")

print("Part 1 Puzzle input found: ", puzzleOutput)

puzzleText.close()

print("Part 2:")

puzzleText = open("./day-1-input.txt", "r")

truePuzzleOutput = 0

strnum = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

for i in range(0, 1000):
    digits = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", puzzleText.readline()) # ?= <- also looks ahead for overlapping matches
    if digits[0].isalpha():
        digits[0] = strnum[digits[0]]
    if digits[-1].isalpha():
        digits[-1] = strnum[digits[-1]]
    currsum = int(digits[0] + digits[-1])
    truePuzzleOutput += currsum
    if debug == "y":
        print(f"{i} : {digits} ({currsum}) -> {truePuzzleOutput}") 

print("Part 2 Puzzle input found: ", truePuzzleOutput)

puzzleText.close()
