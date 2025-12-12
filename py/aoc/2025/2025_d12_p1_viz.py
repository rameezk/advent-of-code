from dataclasses import dataclass
import pygame
import time

from aoc.helper import AOC

COLORS = [
    (231, 76, 60),
    (46, 204, 113),
    (52, 152, 219),
    (155, 89, 182),
    (241, 196, 15),
    (230, 126, 34),
    (26, 188, 156),
    (236, 240, 241),
    (149, 165, 166),
    (52, 73, 94),
]

BACKGROUND = (44, 62, 80)
GRID_COLOR = (52, 73, 94)
EMPTY_COLOR = (189, 195, 199)
SUCCESS_COLOR = (46, 204, 113)
FAIL_COLOR = (231, 76, 60)


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


class Visualizer:
    def __init__(self, width, height, cell_size=40):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.padding = 20

        screen_width = width * cell_size + 2 * self.padding
        screen_height = height * cell_size + 2 * self.padding + 60

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Shape Fitting Visualization")
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)

        self.placements = []
        self.status = None

    def draw_grid(self):
        self.screen.fill(BACKGROUND)

        for r in range(self.height):
            for c in range(self.width):
                x = self.padding + c * self.cell_size
                y = self.padding + r * self.cell_size
                pygame.draw.rect(self.screen, EMPTY_COLOR,
                               (x + 1, y + 1, self.cell_size - 2, self.cell_size - 2))

        for cells, color_idx in self.placements:
            color = COLORS[color_idx % len(COLORS)]
            for r, c in cells:
                x = self.padding + c * self.cell_size
                y = self.padding + r * self.cell_size
                pygame.draw.rect(self.screen, color,
                               (x + 2, y + 2, self.cell_size - 4, self.cell_size - 4))

        for r in range(self.height + 1):
            y = self.padding + r * self.cell_size
            pygame.draw.line(self.screen, GRID_COLOR,
                           (self.padding, y),
                           (self.padding + self.width * self.cell_size, y), 2)
        for c in range(self.width + 1):
            x = self.padding + c * self.cell_size
            pygame.draw.line(self.screen, GRID_COLOR,
                           (x, self.padding),
                           (x, self.padding + self.height * self.cell_size), 2)

        if self.status:
            status_y = self.padding + self.height * self.cell_size + 20
            if self.status == "success":
                text = self.font.render("All shapes fit!", True, SUCCESS_COLOR)
            elif self.status == "fail":
                text = self.font.render("Cannot fit all shapes", True, FAIL_COLOR)
            else:
                text = self.font.render("Solving...", True, (255, 255, 255))
            self.screen.blit(text, (self.padding, status_y))

        pygame.display.flip()

    def add_placement(self, cells, shape_idx):
        self.placements.append((cells, shape_idx))
        self.draw_grid()
        self.handle_events()
        time.sleep(0.05)

    def remove_placement(self):
        if self.placements:
            cells, _ = self.placements[-1]
            for r, c in cells:
                x = self.padding + c * self.cell_size
                y = self.padding + r * self.cell_size
                pygame.draw.rect(self.screen, FAIL_COLOR,
                               (x + 2, y + 2, self.cell_size - 4, self.cell_size - 4))
            pygame.display.flip()
            time.sleep(0.02)
            self.placements.pop()
            self.draw_grid()
            self.handle_events()

    def set_status(self, status):
        self.status = status
        self.draw_grid()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    raise SystemExit

    def wait_for_next(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    raise SystemExit
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        raise SystemExit
                    if event.key == pygame.K_SPACE:
                        waiting = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False
            time.sleep(0.01)


class VisualSolver:
    def __init__(self, shapes, region, visualizer):
        self.shapes = shapes
        self.region = region
        self.width = region.width
        self.height = region.height
        self.occupied = set()
        self.visualizer = visualizer
        self.backtrack_count = 0

    def can_solve(self):
        presents = [idx for idx, qty in enumerate(self.region.quantities) for _ in range(qty)]
        if not presents:
            return True

        total_shape_area = sum(self.shapes[idx].size for idx in presents)
        if total_shape_area > self.width * self.height:
            return False

        sorted_presents = sorted(presents, key=lambda x: -self.shapes[x].size)
        return self._backtrack(sorted_presents)

    def _get_valid_placements(self, shape):
        for orientation, max_r, max_c in shape.orientations:
            for offset_r in range(self.height - max_r):
                for offset_c in range(self.width - max_c):
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

    def _backtrack(self, sorted_presents, idx=0):
        if idx == len(sorted_presents):
            return True

        shape_idx = sorted_presents[idx]
        shape = self.shapes[shape_idx]

        for orientation, offset_r, offset_c in self._get_valid_placements(shape):
            placed = self._try_placement(orientation, offset_r, offset_c)
            self.visualizer.add_placement(placed, shape_idx)

            if self._backtrack(sorted_presents, idx + 1):
                return True

            self._undo_placement(placed)
            self.visualizer.remove_placement()
            self.backtrack_count += 1

        return False


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


@AOC.puzzle(2025, 12, 1)
def solve():
    data = AOC.get_data()

    shapes, regions = parse_input(data)

    print(f"Total regions: {len(regions)}")
    choice = input("Enter region number (1-{}) or 'all' for all regions: ".format(len(regions))).strip().lower()

    if choice == "all":
        selected_regions = list(enumerate(regions))
    else:
        try:
            region_num = int(choice)
            if 1 <= region_num <= len(regions):
                selected_regions = [(region_num - 1, regions[region_num - 1])]
            else:
                print(f"Invalid region number. Must be between 1 and {len(regions)}")
                return
        except ValueError:
            print("Invalid input. Enter a number or 'all'")
            return

    pygame.init()

    valid_count = 0

    for i, region in selected_regions:
        print(f"\nRegion {i + 1}: {region.width}x{region.height}")
        print(f"Shapes to place: {region.quantities}")

        max_dim = max(region.width, region.height)
        cell_size = min(60, max(20, 600 // max_dim))

        visualizer = Visualizer(region.width, region.height, cell_size)
        visualizer.set_status("solving")

        if choice != "all":
            print("  Press SPACE or click to start...")
            visualizer.wait_for_next()

        solver = VisualSolver(shapes, region, visualizer)
        can_fit = solver.can_solve()

        if can_fit:
            valid_count += 1
            visualizer.set_status("success")
            print(f"  -> Shapes fit! (backtracks: {solver.backtrack_count})")
            print("  Press SPACE or click to continue to next region...")
            visualizer.wait_for_next()
        else:
            visualizer.set_status("fail")
            print(f"  -> Shapes don't fit (backtracks: {solver.backtrack_count}, skipping...)")
            time.sleep(0.5)

    pygame.quit()

    print(f"\nTotal valid regions: {valid_count}")


if __name__ == "__main__":
    solve()
