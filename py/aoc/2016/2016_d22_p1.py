from aoc.helper import AOC
import re


@AOC.puzzle(2016, 22, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """root@ebhq-gridcenter# df -h
# Filesystem            Size  Used  Avail  Use%
# /dev/grid/node-x0-y0   10T    8T     2T   80%
# /dev/grid/node-x0-y1   11T    6T     5T   54%
# /dev/grid/node-x0-y2   32T   28T     4T   87%
# /dev/grid/node-x1-y0    9T    7T     2T   77%
# /dev/grid/node-x1-y1    8T    0T     8T    0%
# /dev/grid/node-x1-y2   11T    7T     4T   63%
# /dev/grid/node-x2-y0   10T    6T     4T   60%
# /dev/grid/node-x2-y1    9T    8T     1T   88%
# /dev/grid/node-x2-y2    9T    6T     3T   66%""".splitlines()

    nodes = []
    for line in data:
        if line.startswith('/dev/grid/node'):
            match = re.search(r'node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T', line)
            if match:
                x, y, size, used, avail = map(int, match.groups())
                nodes.append((x, y, size, used, avail))

    count = 0
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if i != j:
                x1, y1, size1, used1, avail1 = nodes[i]
                x2, y2, size2, used2, avail2 = nodes[j]

                if used1 > 0 and used1 <= avail2:
                    count += 1

    print(count)
    AOC.submit_answer(count)


if __name__ == "__main__":
    solve()
