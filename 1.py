import sys

inputs = []
for l in sys.stdin:
    inputs.append(int(l))

target = 2020

for i, n in enumerate(inputs):
    rest = target - n
    if rest in inputs[i:]:
        print("{} * {} = {}".format(n, rest, n * rest))
        break

for i, n in enumerate(inputs):
    rest = target - n
    for j, m in enumerate(inputs[i:]):
        if rest - m in inputs[i + j :]:
            print("{} * {} * {} = {}".format(n, m, rest - m, n * m * (rest - m)))
            sys.exit()