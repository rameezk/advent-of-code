from aoc.helper import AOC


@AOC.puzzle(2016, 9, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """ADVENT"""
#     data = """A(1x5)BC"""
#     data = """(3x3)XYZ"""
#     data = """A(2x2)BCD(2x2)EFG"""
#     data = """(6x1)(1x3)A"""
#     data = """X(8x2)(3x3)ABCY"""

    data = data.replace(' ', '').replace('\n', '').replace('\t', '')

    i = 0
    decompressed_length = 0

    while i < len(data):
        if data[i] == '(':
            marker_end = data.index(')', i)
            marker = data[i+1:marker_end]
            parts = marker.split('x')
            char_count = int(parts[0])
            repeat_count = int(parts[1])

            i = marker_end + 1
            decompressed_length += char_count * repeat_count
            i += char_count
        else:
            decompressed_length += 1
            i += 1

    print(decompressed_length)
    AOC.submit_answer(decompressed_length)


if __name__ == "__main__":
    solve()
