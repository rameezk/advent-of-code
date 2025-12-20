from aoc.helper import AOC


@AOC.puzzle(2019, 8, 1)
def solve():
    data = AOC.get_data().strip()

    width = 25
    height = 6
    layer_size = width * height

    layers = [data[i:i+layer_size] for i in range(0, len(data), layer_size)]

    min_zeros = float('inf')
    result = 0

    for layer in layers:
        zeros = layer.count('0')
        if zeros < min_zeros:
            min_zeros = zeros
            ones = layer.count('1')
            twos = layer.count('2')
            result = ones * twos

    answer = result
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
