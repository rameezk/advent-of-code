from aoc.helper import download_input, submit_answer


def get_pos(n: int) -> (int, int):
    if n == 0:
        raise RuntimeError("Cannot be bro")

    if n == 1:
        return 0, 0

    d, r = divmod(n, 9)
    print(d, r)

    return 0, 0


def manhattan_distance(x: int, y: int) -> int:
    return abs(x) + abs(y)


if __name__ == "__main__":
    print(get_pos(23))
