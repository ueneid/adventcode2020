import sys
from functools import reduce

grid_map = []

for l in sys.stdin:
    grid_map.append(list(l.strip()))

SPACE = "."
TREE = "#"


def part1(grid_map, moving_rule):
    map_height = len(grid_map)
    map_length = len(grid_map[0])
    pointer = [0, 0]
    tree_counter = 0
    while pointer[1] < map_height:
        if grid_map[pointer[1]][pointer[0]] == TREE:
            tree_counter += 1
        pointer = [
            (pointer[0] + moving_rule[0]) % map_length,
            pointer[1] + moving_rule[1],
        ]
    return tree_counter


print(part1(grid_map, (3, 1)))
print(
    reduce(
        lambda a, b: a * b,
        [
            f(rule)
            for rule in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
            for f in [lambda r: part1(grid_map, r)]
        ],
    )
)
