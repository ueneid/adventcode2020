import os
import copy

current_dir: str = os.path.dirname(__file__)
seat_layout: list[list[str]] = []
with open(os.path.join(current_dir, "input.txt")) as file:
    seat_layout += [list(f.strip()) for f in file]


EMPTY: str = "L"
FLOOR: str = "."
OCCUPIED: str = "#"


def print_layout(layout):
    tmp = [col for col in ["".join(row) for row in layout]]
    print("\n".join(tmp), "\n")


def count_adjacent_occupied_seats(layout: list[list[str]], i: int, j: int) -> int:
    h = len(layout)
    w = len(layout[0])
    counter = 0
    if i > 0 and layout[i - 1][j] == OCCUPIED:
        counter += 1
    if i > 0 and j + 1 < w and layout[i - 1][j + 1] == OCCUPIED:
        counter += 1
    if j + 1 < w and layout[i][j + 1] == OCCUPIED:
        counter += 1
    if i + 1 < h and j + 1 < w and layout[i + 1][j + 1] == OCCUPIED:
        counter += 1
    if i + 1 < h and layout[i + 1][j] == OCCUPIED:
        counter += 1
    if i + 1 < h and j > 0 and layout[i + 1][j - 1] == OCCUPIED:
        counter += 1
    if j > 0 and layout[i][j - 1] == OCCUPIED:
        counter += 1
    if i > 0 and j > 0 and layout[i - 1][j - 1] == OCCUPIED:
        counter += 1
    return counter


def count_seen_occupied_seats(layout: list[list[str]], i: int, j: int) -> int:
    h = len(layout)
    w = len(layout[0])
    counter = 0
    offset_i = 1
    offset_j = 1
    while i - offset_i >= 0:
        if layout[i - offset_i][j] == EMPTY:
            break
        if layout[i - offset_i][j] == OCCUPIED:
            counter += 1
            break
        offset_i += 1
    offset_i = 1
    while i - offset_i >= 0 and j + offset_j < w:
        if layout[i - offset_i][j + offset_j] == EMPTY:
            break
        if layout[i - offset_i][j + offset_j] == OCCUPIED:
            counter += 1
            break
        offset_i += 1
        offset_j += 1
    offset_i = 1
    offset_j = 1
    while j + offset_j < w:
        if layout[i][j + offset_j] == EMPTY:
            break
        if layout[i][j + offset_j] == OCCUPIED:
            counter += 1
            break
        offset_j += 1
    offset_j = 1
    while i + offset_i < h and j + offset_j < w:
        if layout[i + offset_i][j + offset_j] == EMPTY:
            break
        if layout[i + offset_i][j + offset_j] == OCCUPIED:
            counter += 1
            break
        offset_i += 1
        offset_j += 1
    offset_i = 1
    offset_j = 1
    while i + offset_i < h:
        if layout[i + offset_i][j] == EMPTY:
            break
        if layout[i + offset_i][j] == OCCUPIED:
            counter += 1
            break
        offset_i += 1
    offset_i = 1
    while i + offset_i < h and j - offset_j >= 0:
        if layout[i + offset_i][j - offset_j] == EMPTY:
            break
        if layout[i + offset_i][j - offset_j] == OCCUPIED:
            counter += 1
            break
        offset_i += 1
        offset_j += 1
    offset_i = 1
    offset_j = 1
    while j - offset_j >= 0:
        if layout[i][j - offset_j] == EMPTY:
            break
        if layout[i][j - offset_j] == OCCUPIED:
            counter += 1
            break
        offset_j += 1
    offset_j = 1
    while i - offset_i >= 0 and j - offset_j >= 0:
        if layout[i - offset_i][j - offset_j] == EMPTY:
            break
        if layout[i - offset_i][j - offset_j] == OCCUPIED:
            counter += 1
            break
        offset_i += 1
        offset_j += 1
    return counter


def empty_seat(layout: list[list[str]], count_func) -> (list[list[str]], int):
    new_layout = copy.deepcopy(layout)
    change_count = 0
    for i, row in enumerate(layout):
        for j, seat in enumerate(row):
            if seat != EMPTY:
                continue
            if count_func(layout, i, j) == 0:
                new_layout[i][j] = OCCUPIED
                change_count += 1
    return new_layout, change_count


def occupy_seat(layout: list[list[str]], count_func, limit) -> (list[list[str]], int):
    new_layout = copy.deepcopy(layout)
    change_count = 0
    for i, row in enumerate(layout):
        for j, seat in enumerate(row):
            if seat != OCCUPIED:
                continue
            if count_func(layout, i, j) >= limit:
                new_layout[i][j] = EMPTY
                change_count += 1
    return new_layout, change_count


def count_occupied_seat(layout: list[list[str]]) -> int:
    return len([seat for row in layout for seat in row if seat == OCCUPIED])


def part1(layout: list[list[str]], count_func):
    while True:
        layout, change_count = empty_seat(layout, count_func)
        if change_count == 0:
            return count_occupied_seat(layout)
        layout, change_count = occupy_seat(layout, count_func, 4)
        if change_count == 0:
            return count_occupied_seat(layout)


def part2(layout: list[list[str]], count_func):
    while True:
        layout, change_count = empty_seat(layout, count_func)
        if change_count == 0:
            return count_occupied_seat(layout)
        layout, change_count = occupy_seat(layout, count_func, 5)
        if change_count == 0:
            return count_occupied_seat(layout)


print(part1(copy.deepcopy(seat_layout), count_adjacent_occupied_seats))
print(part2(copy.deepcopy(seat_layout), count_seen_occupied_seats))