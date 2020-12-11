import os

current_dir: str = os.path.dirname(__file__)
numbers: list[int] = []
with open(os.path.join(current_dir, "input.txt")) as file:
    numbers = [int(f.strip()) for f in file]


def part1(numbers: list[int], preamble_length: int) -> int:
    offset = 0
    target = 0
    while subset := numbers[offset : offset + preamble_length + 1]:
        target = subset.pop()
        for n in subset:
            rest = target - n
            if rest in subset and n != rest:
                offset += 1
                break
        else:
            return target


def part2(numbers: list[int], target: int):
    total = start = end = 0
    while total != target:
        if total < target:
            end += 1
        else:
            start += 1
            end = start + 1
        total = sum(numbers[start:end])
    return min(numbers[start:end]) + max(numbers[start:end])

    # My first attempt is not efficient...
    # offset = 0
    # while True:
    #     history = []
    #     if offset >= len(numbers):
    #         return 0
    #     for n in numbers[offset:]:
    #         history.append(n)
    #         if sum(history) == target:
    #             return min(history) + max(history)
    #     offset += 1


invalid_number = part1(numbers, 25)
print(invalid_number)
print(part2(numbers, invalid_number))
