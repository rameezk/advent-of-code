from aoc.helper import AOC

@AOC.puzzle(2020, 16, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50
#
# your ticket:
# 7,1,14
#
# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12"""

    sections = data.split("\n\n")
    rules_section = sections[0]
    nearby_section = sections[2]

    ranges = []
    for line in rules_section.split("\n"):
        parts = line.split(": ")[1]
        range_parts = parts.split(" or ")
        for rp in range_parts:
            low, high = map(int, rp.split("-"))
            ranges.append((low, high))

    nearby_tickets = []
    for line in nearby_section.split("\n")[1:]:
        ticket = list(map(int, line.split(",")))
        nearby_tickets.append(ticket)

    error_rate = 0
    for ticket in nearby_tickets:
        for value in ticket:
            valid = False
            for low, high in ranges:
                if low <= value <= high:
                    valid = True
                    break
            if not valid:
                error_rate += value

    answer = error_rate
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
