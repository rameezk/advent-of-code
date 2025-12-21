from aoc.helper import AOC
import json


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


@AOC.puzzle(2022, 13, 1)
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

    pairs = data.split('\n\n')

    correct_indices = []

    for idx, pair in enumerate(pairs, 1):
        lines = pair.strip().split('\n')
        left = json.loads(lines[0])
        right = json.loads(lines[1])

        if compare(left, right) == -1:
            correct_indices.append(idx)

    result = sum(correct_indices)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
