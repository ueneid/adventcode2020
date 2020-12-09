import os
import re


current_dir: str = os.path.dirname(__file__)
outermost_bags: dict[str, list[tuple[int, str]]] = {}
with open(os.path.join(current_dir, "input.txt")) as file:
    for f in file:
        outermost, bags = [
            outermost_and_bags for outermost_and_bags in f.split(" bags contain ")
        ]
        outermost_bags[outermost] = []
        m = re.fullmatch(r"(^.+)\sbags?$", outermost)
        pat = re.compile(r"(\d+)\s(.+?)\sbags*")
        for num, color in re.findall(pat, bags):
            outermost_bags[outermost].append((int(num), color))

target: str = "shiny gold"


def part1(bags: dict[str, list[tuple[int, str]]], target: str):
    def helper(color: str):
        if color == target:
            return 1
        return any(helper(clr) for _, clr in bags[color])

    return sum(helper(color) for color in bags) - 1


print(part1(outermost_bags, target))


def part2(bags: dict[str, list[tuple[int, str]]], target: str):
    def helper(color: str):
        return 1 + sum(n * helper(clr) for n, clr in bags[color])

    return helper(target) - 1


print(part2(outermost_bags, target))