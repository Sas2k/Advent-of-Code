"""
- Advent of Code 2024 -
-       Day 5         -
: Sas2k
"""
from collections import defaultdict

print("Advent of Code 2024 - Day 5")
debug = input("Do you wish to see the debug statements[y/n]:>")

puzzleInput = open("./day-5-input.txt", "r")
fileLen = sum(1 for _ in open('./day-5-input.txt'))


def topologicalSort(nodes: dict[int, list[int]]) -> list[int]:
    """
    Topological sort for a network of nodes

        nodes = {1: [2, 3], 2: [], 3: [2]}
        topological_sort(nodes)
        # [1, 3, 2]

    :param nodes: Nodes of the network
    :return: nodes in topological order
    """

    # Calculate the indegree for each node
    indegrees = {k: 0 for k in nodes.keys()}
    for name, dependencies in nodes.items():
        for dependency in dependencies:
            try:
                indegrees[dependency] += 1
            except KeyError:
                indegrees[dependency] = 0

    # Place all elements with indegree 0 in queue
    queue = [k for k in nodes.keys() if indegrees[k] == 0]

    final_order = []

    # Continue until all nodes have been dealt with
    while len(queue) > 0:

        # node of current iteration is the first one from the queue
        curr = queue.pop(0)
        final_order.append(curr)

        # remove the current node from other dependencies
        for dependency in nodes[curr]:
            indegrees[dependency] -= 1

            if indegrees[dependency] == 0:
                queue.append(dependency)

    # check for circular dependencies
    if len(final_order) != len(nodes):
        return "Circular dependency found."

    return final_order


def removeUnneccesaryNodes(graph: defaultdict(list), array: list[int]) -> defaultdict(list):
    "Removed the unnecessary nodes based on array"
    curOrder = graph.copy()
    for cur in graph.keys():
        if cur not in line:
            curOrder.pop(cur)
    for key in curOrder.keys():
        if curOrder[key] not in line:
            curOrder[key] = [x for x in curOrder[key] if x in line]

    return curOrder


print("Formatting Data....")

orders = defaultdict(list)
updates = []

puzzleInput.seek(0)

for n in range(0, fileLen):
    curLine = puzzleInput.readline()
    if "|" in curLine:
        orders[int(curLine.split("|")[0])].append(int(curLine.split("|")[1]))
    elif "," in curLine:
        updates.append([int(i) for i in curLine.split(",")])

if debug.lower() == "y":
    print(updates, orders)

print("Main sorted arr -> ", topologicalSort(orders))

puzzleInput.close()
print("Formatted....")

print("Running Part 1....")
puzzle1Output = 0

for line in updates:
    # remove unneccesary nodes
    curOrder = removeUnneccesaryNodes(orders, line)
    sorts = topologicalSort(curOrder)

    iA = 0
    iB = 0
    safe = 0
    while iA < len(line) and iB < len(sorts):
        if line[iA] == sorts[iB]:
            iA += 1
            iB += 1
            safe += 1
        else:
            iB += 1
    if safe == len(line):
        if debug.lower() == "y":
            print("Sorted -> ", sorts)
            print("Safe -> ", line, " : Mid =", line[len(line)//2])
        puzzle1Output += line[len(line)//2]

print(f"Part 1 Puzzle Output -> {puzzle1Output}")


print("Running Part 2....")
puzzle2Output = 0

for line in updates:
    # remove unneccesary nodes
    curOrder = removeUnneccesaryNodes(orders, line)
    sorts = topologicalSort(curOrder)

    if debug.lower() == "y":
        print("Cur Orderr -> ", curOrder)
        print("Sorted -> ", sorts)

    iA = 0
    iB = 0
    safe = 0
    while iA < len(line) and iB < len(sorts):
        if line[iA] == sorts[iB]:
            iA += 1
            iB += 1
            safe += 1
        else:
            iB += 1
    if safe != len(line):
        if debug.lower() == "y":
            print("Corrected Array -> ", sorts)
            print("Unsafe -> ", line, " : Mid =", line[len(line)//2])
        puzzle2Output += sorts[len(sorts)//2]

print(f"Part 2 Puzzle Output -> {puzzle2Output}")
