from dataclasses import dataclass

from aoc.helper import AOC


@dataclass
class Region:
    width: int
    height: int
    quantities: list[int]


class Shape:
    def __init__(self, coords):
        self.coords = self._normalize(frozenset(coords))
        self.size = len(self.coords)
        self.orientations = self._compute_orientations()

    @classmethod
    def from_lines(cls, lines):
        coords = set()
        for r, line in enumerate(lines):
            for c, char in enumerate(line):
                if char == "#":
                    coords.add((r, c))
        return cls(coords)

    @staticmethod
    def _normalize(coords):
        min_r = min(r for r, c in coords)
        min_c = min(c for r, c in coords)
        return frozenset((r - min_r, c - min_c) for r, c in coords)

    @staticmethod
    def _rotate_90(coords):
        rotated = frozenset((c, -r) for r, c in coords)
        return Shape._normalize(rotated)

    @staticmethod
    def _flip_horizontal(coords):
        flipped = frozenset((r, -c) for r, c in coords)
        return Shape._normalize(flipped)

    def _compute_orientations(self):
        orientations = set()
        current = self.coords
        for _ in range(4):
            orientations.add(current)
            orientations.add(Shape._flip_horizontal(current))
            current = Shape._rotate_90(current)

        result = []
        for orient in orientations:
            max_r = max(r for r, c in orient)
            max_c = max(c for r, c in orient)
            result.append((orient, max_r, max_c))
        return result

    @staticmethod
    def can_place(orientation, offset_r, offset_c, occupied, width, height):
        for r, c in orientation:
            nr, nc = r + offset_r, c + offset_c
            if nr < 0 or nr >= height or nc < 0 or nc >= width:
                return False
            if (nr, nc) in occupied:
                return False
        return True

    @staticmethod
    def place(orientation, offset_r, offset_c):
        return {(r + offset_r, c + offset_c) for r, c in orientation}


class Solver:
    def __init__(self, shapes, region):
        self.shapes = shapes
        self.region = region
        self.width = region.width
        self.height = region.height
        self.occupied = set()

    def can_solve(self):
        presents = [idx for idx, qty in enumerate(self.region.quantities) for _ in range(qty)]
        if not presents:
            return True

        total_shape_area = sum(self.shapes[idx].size for idx in presents)
        if total_shape_area > self.width * self.height:
            return False

        sorted_presents = sorted(presents, key=lambda x: -self.shapes[x].size)
        return self._backtrack(sorted_presents)

    def _get_valid_placements(self, shape, min_pos):
        for orientation, max_r, max_c in shape.orientations:
            for offset_r in range(self.height - max_r):
                for offset_c in range(self.width - max_c):
                    if (offset_r, offset_c) < min_pos:
                        continue
                    if Shape.can_place(
                        orientation,
                        offset_r,
                        offset_c,
                        self.occupied,
                        self.width,
                        self.height,
                    ):
                        yield orientation, offset_r, offset_c

    def _try_placement(self, orientation, offset_r, offset_c):
        placed = Shape.place(orientation, offset_r, offset_c)
        self.occupied.update(placed)
        return placed

    def _undo_placement(self, placed):
        self.occupied.difference_update(placed)

    def _backtrack(self, sorted_presents, idx=0, min_pos=(0, 0)):
        if idx == len(sorted_presents):
            return True

        shape = self.shapes[sorted_presents[idx]]
        is_same_as_prev = idx > 0 and sorted_presents[idx] == sorted_presents[idx - 1]
        next_min = min_pos if is_same_as_prev else (0, 0)

        for orientation, offset_r, offset_c in self._get_valid_placements(
            shape, next_min
        ):
            placed = self._try_placement(orientation, offset_r, offset_c)
            if self._backtrack(sorted_presents, idx + 1, (offset_r, offset_c)):
                return True
            self._undo_placement(placed)

        return False


@AOC.puzzle(2025, 12, 1)
def solve():
    data = AOC.get_data()

#     data = """0:
# ###
# ##.
# ##.
#
# 1:
# ###
# ##.
# .##
#
# 2:
# .##
# ###
# ##.
#
# 3:
# ##.
# ###
# ##.
#
# 4:
# ###
# #..
# ###
#
# 5:
# ###
# .#.
# ###
#
# 4x4: 0 0 0 0 2 0
# 12x5: 1 0 1 0 2 2
# 12x5: 1 0 1 0 3 2"""

    shapes, regions = parse_input(data)
    valid_count = sum(1 for region in regions if Solver(shapes, region).can_solve())

    print(valid_count)
    AOC.submit_answer(valid_count)


def parse_input(data):
    sections = data.strip().split("\n\n")

    shapes = {}
    for section in sections[:-1]:
        lines = section.strip().splitlines()
        index = int(lines[0].rstrip(":"))
        shapes[index] = Shape.from_lines(lines[1:])

    regions = []
    for line in sections[-1].strip().splitlines():
        size_part, quantities_part = line.split(":")
        width, height = map(int, size_part.split("x"))
        quantities = list(map(int, quantities_part.strip().split()))
        regions.append(Region(width, height, quantities))

    return shapes, regions


if __name__ == "__main__":
    solve()
