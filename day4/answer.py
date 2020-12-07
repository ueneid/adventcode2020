import sys
import re

inputs = []

counter = 0
for l in sys.stdin:
    values = l.strip().split()
    if not values:
        counter += 1
        continue
    d = {k: v for k, v in [v.split(":") for v in values]}
    if len(inputs) == counter:
        inputs.append(d)
    else:
        inputs[counter].update(d)

FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid",
]
len_fields = len(FIELDS)


def part1(passports):
    valid_counter = 0
    for p in passports:
        len_p = len(p)
        if len_p < len_fields - 1:
            continue
        if len_p == len_fields - 1 and "cid" in p:
            continue
        valid_counter += 1
    return valid_counter


print(part1(inputs))


EYECOLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def part2(passports):
    valid_counter = 0
    r = re.compile(r"(cm|in)$")
    for a, b, c, d, e, f, g, h in passports:
        print(a)
    for p in passports:
        len_p = len(p)
        if len_p < len_fields - 1:
            continue
        if len_p == len_fields - 1 and "cid" in p:
            continue
        if not (len(p["byr"]) == 4 and 1920 <= int(p["byr"]) <= 2002):
            continue
        if not (len(p["iyr"]) == 4 and 2010 <= int(p["iyr"]) <= 2020):
            continue
        if not (len(p["eyr"]) == 4 and 2020 <= int(p["eyr"]) <= 2030):
            continue
        m = r.search(p["hgt"])
        if m is None:
            continue
        if m.group() == "cm" and not (150 <= int(p["hgt"][:-2]) <= 193):
            continue
        if m.group() == "in" and not (59 <= int(p["hgt"][:-2]) <= 76):
            continue
        if not (re.fullmatch(r"^#[0-9a-z]{6}$", p["hcl"])):
            continue
        if p["ecl"] not in EYECOLORS:
            continue
        if not re.fullmatch(r"^[0-9]{9}$", p["pid"]):
            continue
        valid_counter += 1
    return valid_counter


print(part2(inputs))