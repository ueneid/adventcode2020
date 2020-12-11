import os
from dataclasses import dataclass, field
import copy


@dataclass
class BootCode:
    command: str
    value: int
    visited: bool = False


@dataclass
class BootLoader:
    codes: list[BootCode]
    accumulator: int = 0
    cursor: int = 0

    def run(self) -> int:
        code = self.codes[self.cursor]
        if code.visited:
            return self.accumulator
        code.visited = True
        self.execute(code)
        return self.run()

    def execute(self, code):
        if code.command == "nop":
            self.cursor += 1
        if code.command == "acc":
            self.cursor += 1
            self.accumulator += code.value
        if code.command == "jmp":
            self.cursor += code.value

    def check(self):
        code = self.codes[self.cursor]
        if code.visited:
            return False
        code.visited = True
        self.execute(code)
        if self.cursor == len(self.codes):
            return True
        return self.check()


current_dir: str = os.path.dirname(__file__)
codes: list[BootCode] = []
with open(os.path.join(current_dir, "input.txt")) as file:
    codes = [
        BootCode(command=c, value=int(a), visited=False)
        for c, a in [f.strip().split() for f in file]
    ]


def part1(codes: list[BootCode]):
    bootloader = BootLoader(codes)
    return bootloader.run()


def part2(codes: list[BootCode]):
    for index, code in enumerate(codes):
        if code.command == "acc":
            continue
        new_codes = copy.deepcopy(codes)
        new_codes[index].command = "nop" if new_codes[index].command == "jmp" else "jmp"
        bootloader = BootLoader(new_codes)
        if bootloader.check():
            return bootloader.accumulator


print(part1(copy.deepcopy(codes)))
print(part2(codes))