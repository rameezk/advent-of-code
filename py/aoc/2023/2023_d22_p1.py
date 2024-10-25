from aoc.helper import download_input, submit_answer
from aoc.util import benchmark


def print_bricks(bricks, orientation):
    if orientation == "x":
        for label, (start, end) in bricks.items():
            sx, sy, sz = start
            ex, ey, ez = end
            print(label, start, end)


@benchmark
def run():
    download_input(2023, 22)

    snapshot = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
    """.strip().splitlines()

    labels = [chr(o) for o in range(65, 65 + len(snapshot))]

    bricks = {}
    for label, snap in zip(labels, snapshot):
        start, end = snap.split("~")
        start = list(map(int, start.split(",")))
        end = list(map(int, end.split(",")))
        bricks[label] = [start, end]

    print_bricks(bricks, orientation="x")


if __name__ == "__main__":
    run()
