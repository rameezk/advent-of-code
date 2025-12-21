from aoc.helper import AOC
import json
from functools import cmp_to_key


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0

    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            result = compare(left[i], right[i])
            if result != 0:
                return result

        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return 1
        else:
            return 0

    if isinstance(left, int):
        return compare([left], right)
    else:
        return compare(left, [right])


@AOC.puzzle(2022, 13, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """[1,1,3,1,1]
# [1,1,5,1,1]
#
# [[1],[2,3,4]]
# [[1],4]
#
# [9]
# [[8,7,6]]
#
# [[4,4],4,4]
# [[4,4],4,4,4]
#
# [7,7,7,7]
# [7,7,7]
#
# []
# [3]
#
# [[[]]]
# [[]]
#
# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]"""

    packets = []
    for line in data.split('\n'):
        if line.strip():
            packets.append(json.loads(line))

    divider1 = [[2]]
    divider2 = [[6]]
    packets.append(divider1)
    packets.append(divider2)

    packets.sort(key=cmp_to_key(compare))

    idx1 = packets.index(divider1) + 1
    idx2 = packets.index(divider2) + 1

    result = idx1 * idx2
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
