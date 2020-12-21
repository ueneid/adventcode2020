import os

current_dir: str = os.path.dirname(__file__)
inputs = []
with open(os.path.join(current_dir, "input.txt")) as file:
    inputs = sum([list(map(int, f.strip().split(","))) for f in file], [])


def answer(inputs: list, limit: int) -> int:
    len_n = len(inputs)
    cache = {}
    history = []
    for turn in range(limit):
        if turn < len_n:
            if history:
                cache[inputs[turn - 1]] = turn
            history.append(inputs[turn])
            continue
        prev = history[turn - 1]
        if prev in cache:
            history.append(turn - cache[prev])
            cache[prev] = turn
        else:
            history.append(0)
            cache[prev] = turn
    return history[-1]


print(answer(inputs, 2020))
print(answer(inputs, 30000000))
