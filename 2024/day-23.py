"""
- Advent of Code 2024 -
-       Day 23        -
: Sas2k
"""
import networkx as nx

print("Advent of Code - Day 23")

puzzleInput = open("./day-23-input.txt", "r")
fileLen = sum(1 for _ in open("./day-23-input.txt"))

print("Formatting Data....")
G = nx.Graph()

for i in range(fileLen):
    data = puzzleInput.readline().strip().split("-")
    G.add_edge(data[0], data[1])

print('Part 1 Complete....')
puzzle1Output = 0

for clique in nx.clique.enumerate_all_cliques(G):
    if len(clique) == 3:
        puzzle1Output += 1 if "t" in [node[0] for node in clique] else 0

print(f'Part 1 Puzzle Output -> {puzzle1Output}')

print(f'Part 2 Puzzle Output -> {",".join(sorted(clique))}')
