import os

current_dir: str = os.path.dirname(__file__)
rules = {}
your_tickets = []
nearby_tickets = []
valid_nums = set()
with open(os.path.join(current_dir, "input.txt")) as file:
    input_type = "rule"
    for f in file:
        f = f.strip()
        if not f:
            continue
        if f.startswith("your ticket"):
            input_type = "your"
        elif f.startswith("nearby tickets"):
            input_type = "nearby"
        elif input_type == "your":
            your_tickets = tuple(map(int, f.split(",")))
        elif input_type == "nearby":
            nearby_tickets.append(tuple(map(int, f.split(","))))
        elif input_type == "rule":
            field, rule_desc = f.split(": ")
            r = set()
            for rule in rule_desc.split(" or "):
                mi, ma = map(int, rule.split("-"))
                r |= set(range(mi, ma + 1))
            rules[field] = r

    for r in rules.values():
        valid_nums |= r


def part1(rules: list[tuple], nearby_tickets: list[tuple]) -> int:
    error_rate = 0
    for nearby in nearby_tickets:
        for n in nearby:
            if n not in valid_nums:
                error_rate += n
    return error_rate


print(part1(rules, nearby_tickets))