from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2016, 3)

    with open("./2016_d03.txt") as f:
        triangles = f.read().strip().splitlines()

    # triangles = ["5 10 25"]

    valid = 0
    for triangle in triangles:
        sides = sorted([int(n) for n in triangle.split()])
        if sides[0] + sides[1] > sides[2]:
            valid += 1

    print(valid)
    # submit_answer(2016, 3, 1, valid)
