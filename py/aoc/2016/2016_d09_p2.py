from aoc.helper import AOC


def get_decompressed_length(data):
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
            section = data[i:i+char_count]
            section_length = get_decompressed_length(section)
            decompressed_length += section_length * repeat_count
            i += char_count
        else:
            decompressed_length += 1
            i += 1

    return decompressed_length


@AOC.puzzle(2016, 9, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """(3x3)XYZ"""
#     data = """X(8x2)(3x3)ABCY"""
#     data = """(27x12)(20x12)(13x14)(7x10)(1x12)A"""
#     data = """(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"""

    result = get_decompressed_length(data)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
