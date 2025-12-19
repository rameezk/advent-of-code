from aoc.helper import AOC


@AOC.puzzle(2016, 16, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """10000"""

    def dragon_step(a):
        b = a[::-1]
        b = ''.join('1' if c == '0' else '0' for c in b)
        return a + '0' + b

    def fill_disk(initial, disk_length):
        data = initial
        while len(data) < disk_length:
            data = dragon_step(data)
        return data[:disk_length]

    def checksum(data):
        result = data
        while len(result) % 2 == 0:
            new_result = []
            for i in range(0, len(result), 2):
                if result[i] == result[i+1]:
                    new_result.append('1')
                else:
                    new_result.append('0')
            result = ''.join(new_result)
        return result

    disk_length = 35651584
    filled = fill_disk(data, disk_length)
    answer = checksum(filled)

    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
