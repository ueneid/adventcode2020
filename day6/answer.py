import os

current_dir: str = os.path.dirname(__file__)

inputs = []
with open(os.path.join(current_dir, "input.txt")) as file:
    inputs = [f.strip() for f in file]


def part1(answers: list[dict[str, int]]) -> int:
    return len([k for i in answers for k in i.keys() if k != "cnt"])


def part2(answers: list[dict[str, int]]) -> int:
    return len(
        [k for i in answers for k, v in i.items() if k != "cnt" and v == i["cnt"]]
    )


answers: list[dict[str, int]] = []
pointer = 0
for i in inputs:
    if not i:
        pointer += 1
        d = {}
        continue
    d: dict[str, int] = {s: 1 for s in list(i)}
    if len(answers) == pointer:
        d["cnt"] = 1
        answers.append(d)
    else:
        for k, v in d.items():
            if k in answers[pointer]:
                answers[pointer][k] += 1
            else:
                answers[pointer][k] = v
        answers[pointer]["cnt"] += 1


print(part1(answers))
print(part2(answers))