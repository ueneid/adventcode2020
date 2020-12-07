import sys

inputs = []
for l in sys.stdin:
    inputs.append(
        l.strip().translate(str.maketrans({"F": "0", "L": "0", "B": "1", "R": "1"}))
    )


def decode(seat_str: str) -> int:
    def helper(seat_str: str, min_n: int, max_n: int) -> int:
        for c in seat_str:
            mid = (max_n - min_n) // 2
            if c == "0":
                max_n = min_n + mid
            else:
                min_n = min_n + mid + 1
        return min_n

    row_number = helper(seat_str[:7], 0, 127)
    column_number = helper(seat_str[7:], 0, 7)
    return row_number * 8 + column_number


seat_ids = list(map(decode, inputs))
assert len(seat_ids) == len(set(seat_ids))
print(max(seat_ids))

l = len(seat_ids)
sorted_seat_ids = sorted(seat_ids)
for i, sid in enumerate(sorted_seat_ids[:-1]):
    if sid + 1 != sorted_seat_ids[i + 1]:
        print(sid + 1)
        break
