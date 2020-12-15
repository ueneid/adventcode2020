import os

current_dir: str = os.path.dirname(__file__)
inputs: list[list[str]] = []
with open(os.path.join(current_dir, "input.txt")) as file:
    inputs = [(inst[:1], int(inst[1:])) for inst in [f.strip() for f in file]]

direction_map = ["N", "E", "S", "W"]


def move(pos: list[int], action: str, value: int) -> list[int]:
    if action == "N":
        pos[1] += value
    elif action == "S":
        pos[1] -= value
    elif action == "E":
        pos[0] += value
    elif action == "W":
        pos[0] -= value
    return pos


def part1(instructions: list[tuple]) -> int:
    pos = [0, 0]
    direction = 90
    for action, value in instructions:
        if action in direction_map:
            pos = move(pos, action, value)
        elif action == "F":
            pos = move(pos, direction_map[(direction % 360) // 90], value)
        elif action == "L":
            direction -= value
        elif action == "R":
            direction += value

    return sum(map(abs, pos))


print(part1(inputs))


def part2(instructions: list[tuple]) -> int:
    pos = [0, 0]
    waypoint = [10, 1]
    for action, value in instructions:
        if action in direction_map:
            waypoint = move(waypoint, action, value)
        elif action == "F":
            pos = [p + w for p, w in zip(pos, map(lambda n: n * value, waypoint))]
        elif action == "L":
            for _ in range(value // 90):
                waypoint = [-waypoint[1], waypoint[0]]
        elif action == "R":
            for _ in range(value // 90):
                waypoint = [waypoint[1], -waypoint[0]]
    return sum(map(abs, pos))


print(part2(inputs))