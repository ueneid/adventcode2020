import sys

inputs = []

for l in sys.stdin:
    policy, password = [s.strip() for s in l.split(":")]
    min_max, c = [s for s in policy.split()]
    min_count, max_count = map(int, min_max.split("-"))
    inputs.append((min_count, max_count, c, password))

counter = 0
for min_count, max_count, c, password in inputs:
    if min_count <= password.count(c) <= max_count:
        print(min_count, max_count, c, password)
        counter += 1

print(counter)

counter = 0
for p1, p2, c, password in inputs:
    s1, s2 = password[p1 - 1], password[p2 - 1]
    if (s1 == c or s2 == c) and s1 != s2:
        print(p1, p2, c, password)
        counter += 1

print(counter)