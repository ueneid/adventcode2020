import os
from functools import reduce

current_dir: str = os.path.dirname(__file__)
inputs: list[str] = []
estimated_departing_time = 0
with open(os.path.join(current_dir, "input.txt")) as file:
    estimated_departing_time = int(file.readline().strip())
    inputs = [id for id in file.readline().split(",")]


def part1(inputs: list[str]) -> int:
    without_x = [int(id) for id in inputs if id != "x"]
    min_bus = sorted(
        [(id, id - (estimated_departing_time % id)) for id in without_x],
        key=lambda x: x[1],
    )[0]
    return min_bus[0] * min_bus[1]


print(part1(inputs))


def part2(inputs: list[str]) -> int:
    # The two functions below are
    # from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
    def chinese_remainder(n, a):
        sum = 0
        prod = reduce(lambda a, b: a * b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * mul_inv(p, n_i) * p
        return sum % prod

    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1

    ids = []
    mods = []
    offset = 0
    for id in inputs:
        if id != "x":
            ids.append(int(id))
            mods.append(int(id) - offset)
        offset += 1
    return chinese_remainder(ids, mods)


print(part2(inputs))