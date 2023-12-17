from aoc.helper import download_input, submit_answer
from aoc.util import benchmark

from heapq import heappush, heappop


def calculate_min_heat_loss(city_block) -> int:
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        hl, r, c, dr, dc, n = heappop(pq)

        if r == len(city_block) - 1 and c == len(city_block[0]) - 1:
            return hl

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))

        if n < 3 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(city_block) and 0 <= nc < len(city_block[0]):
                heappush(pq, (hl + city_block[nr][nc], nr, nc, dr, dc, n + 1))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                nr = r + ndr
                nc = c + ndc
                if 0 <= nr < len(city_block) and 0 <= nc < len(city_block[0]):
                    heappush(pq, (hl + city_block[nr][nc], nr, nc, ndr, ndc, 1))

    return 0


@benchmark
def run():
    download_input(2023, 17)

    city_block = """
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
    """.strip().splitlines()

    with open("./2023_d17.txt") as f:
        city_block = f.read().strip().splitlines()

    city_block = [list(map(int, c)) for c in city_block]

    heat_loss = calculate_min_heat_loss(city_block)
    print(heat_loss)
    # submit_answer(2023, 17, 1, heat_loss)


if __name__ == "__main__":
    run()
