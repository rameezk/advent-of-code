from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2018, 1)

    with open("./2018_d01.txt") as f:
        data = f.read()

    f = 0
    for line in data.strip().splitlines():
        line = line.strip()
        operator = line[0]
        operand = int(line[1::])

        if operator == "+":
            f += operand
        else:
            f -= operand

    print(f)
    # submit_answer(2018, 1, 1, f)
