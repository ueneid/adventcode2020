import os
import re
import itertools

current_dir: str = os.path.dirname(__file__)
inputs = []
with open(os.path.join(current_dir, "input.txt")) as file:
    for line in file:
        var, value = line.strip().split(" = ")
        if var == "mask":
            inputs.append([(var, value)])
        else:
            inputs[-1].append((var, int(value)))


def part1(inputs: list[list[tuple]]) -> int:
    memory = {}
    pat = re.compile(r"^mem\[(\d+)\]")
    for prog in inputs:
        _, mask = prog[0]
        mask0 = int(re.sub(r"[X]", "1", mask), 2)
        mask1 = int(re.sub(r"[X]", "0", mask), 2)
        for var, value in prog[1:]:
            m = pat.match(var)
            init_address = int(m.group(1))
            value = int(value)
            memory[init_address] = value & mask0 | mask1
    return sum(memory.values())


print(part1(inputs))


def part2(inputs: list[list[tuple]]) -> int:
    memory = {}
    pat = re.compile(r"^mem\[(\d+)\]")
    for prog in inputs:
        _, mask = prog[0]
        x_indexes = [i for i, v in enumerate(reversed(mask)) if v == "X"]
        x_combi = list(itertools.product((1, 0), repeat=len(x_indexes)))
        mask1 = int(re.sub(r"[X]", "0", mask), 2)
        for var, value in prog[1:]:
            m = pat.match(var)
            init_address = int(m.group(1)) | mask1
            for comb in x_combi:
                for i, c in enumerate(comb):
                    if c:
                        init_address |= 1 << x_indexes[i]
                    else:
                        init_address &= ~(1 << x_indexes[i])
                memory[init_address] = value
    return sum(memory.values())


print(part2(inputs))