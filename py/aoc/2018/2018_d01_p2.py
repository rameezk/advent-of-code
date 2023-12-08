from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2018, 1)

    with open("./2018_d01.txt") as f:
        data = f.read().strip().splitlines()

    i = 0
    s = len(data)
    f = 0
    fs = [0]
    x = None
    while True:
        if x is not None:
            break

        if i == s:
            i = 0

        item = data[i]
        operator = item[0]
        operand = int(item[1::])

        if operator == "+":
            f += operand
        else:
            f -= operand

        if f in fs:
            x = f
            break

        fs.append(f)
        i += 1

    print(x)
    # submit_answer(2018, 1, 2, x)
