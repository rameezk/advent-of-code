from aoc.helper import AOC
from collections import Counter


@AOC.puzzle(2016, 6, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar""".strip().splitlines()

    message_length = len(data[0])
    result = []

    for i in range(message_length):
        column = [line[i] for line in data]
        counter = Counter(column)
        least_common = counter.most_common()[-1][0]
        result.append(least_common)

    answer = ''.join(result)
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
