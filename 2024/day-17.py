"""
- Advent of Code 2024 -
-       Day 17        -
: Sas2k
"""
from functools import cache

puzzleInput = open("./day-17-input.txt", "r")
fileLen = sum(1 for _ in open("./day-17-input.txt"))

print("Advent of Code 2024 - Day 17")

print("Formatting Data")

InputRegisters = []  # 0 <- A, 1 <- B, 2 <- 3
program = []

for i in range(0, fileLen):
    curLine = puzzleInput.readline()
    if len(curLine) <= 1:
        continue
    if "," not in curLine:
        InputRegisters.append(int(curLine.split(": ")[1].strip()))
    else:
        program = [int(num) for num in curLine[9:].strip().split(",")]


print("Formatted")

print("Running part 1")

pointer = 0
jump = False
puzzle1Output = []
registers = InputRegisters.copy()


def divA(registers: list, store: int, combo: bool, operand):
    "Handles the divistion"
    registers[store] = registers[0] // (2 ** registers[operand %
                                                       4]) if combo else registers[0] // (2 ** operand)


while pointer < len(program):
    opcode = program[pointer]
    combo = program[pointer + 1] >= 4
    operand = program[pointer + 1]
    match opcode:
        case 0:  # adv
            divA(registers, 0, combo, operand)
        case 1:  # bxl
            registers[1] ^= operand
        case 2:  # bst
            registers[1] = registers[operand % 4] % 8 if combo else operand % 8
        case 3:  # jnz
            if registers[0] != 0:
                pointer = operand
                continue
        case 4:  # bxc
            registers[1] ^= registers[2]
        case 5:  # out
            out = registers[operand % 4] % 8 if combo else operand % 8
            puzzle1Output.append(str(out))
        case 6:  # bdv
            divA(registers, 1, combo, operand)
        case 7:
            divA(registers, 2, combo, operand)
    pointer += 2

print(f"Part 1 Puzzle Output -> {",".join(puzzle1Output)}")

print("Part 2 Running....")
puzzle2Output = 0


@cache
def code(val: int) -> list:
    "Python transpilled version of puzzle input"
    registers = [val, 0, 0]
    output = []

    while registers[0] != 0:
        registers[1] = registers[0] % 8
        registers[1] ^= 3

        divA(registers, 2, True, 5)

        registers[1] ^= registers[2]
        registers[1] ^= 3

        divA(registers, 0, False, 3)
        out = registers[1] % 8
        output.append(str(out))

    return output


a = 2 ** (len(program) * 3)
check = False

while not check:
    if code(a) == program:
        break
    a += 1

print(f"Part 2 Puzzle Output -> {i}")
