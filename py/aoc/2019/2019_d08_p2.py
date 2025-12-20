from aoc.helper import AOC


@AOC.puzzle(2019, 8, 2)
def solve():
    data = AOC.get_data().strip()

    width = 25
    height = 6
    layer_size = width * height

    layers = [data[i:i+layer_size] for i in range(0, len(data), layer_size)]

    image = []
    for pos in range(layer_size):
        pixel = '2'
        for layer in layers:
            if layer[pos] != '2':
                pixel = layer[pos]
                break
        image.append(pixel)

    for row in range(height):
        line = ''
        for col in range(width):
            char = image[row * width + col]
            if char == '1':
                line += '#'
            else:
                line += ' '
        print(line)

    answer = input("What letters do you see? ")
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
