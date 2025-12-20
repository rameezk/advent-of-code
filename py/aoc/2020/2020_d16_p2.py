from aoc.helper import AOC

@AOC.puzzle(2020, 16, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """class: 0-1 or 4-19
# row: 0-5 or 8-19
# seat: 0-13 or 16-19
#
# your ticket:
# 11,12,13
#
# nearby tickets:
# 3,9,18
# 15,1,5
# 5,14,9"""

    sections = data.split("\n\n")
    rules_section = sections[0]
    my_ticket_section = sections[1]
    nearby_section = sections[2]

    field_rules = {}
    all_ranges = []
    for line in rules_section.split("\n"):
        field_name, ranges_str = line.split(": ")
        ranges = []
        range_parts = ranges_str.split(" or ")
        for rp in range_parts:
            low, high = map(int, rp.split("-"))
            ranges.append((low, high))
            all_ranges.append((low, high))
        field_rules[field_name] = ranges

    my_ticket = list(map(int, my_ticket_section.split("\n")[1].split(",")))

    nearby_tickets = []
    for line in nearby_section.split("\n")[1:]:
        ticket = list(map(int, line.split(",")))
        nearby_tickets.append(ticket)

    valid_tickets = []
    for ticket in nearby_tickets:
        is_valid = True
        for value in ticket:
            valid = False
            for low, high in all_ranges:
                if low <= value <= high:
                    valid = True
                    break
            if not valid:
                is_valid = False
                break
        if is_valid:
            valid_tickets.append(ticket)

    num_fields = len(my_ticket)
    possible_fields = {}
    for i in range(num_fields):
        possible_fields[i] = set(field_rules.keys())

    for ticket in valid_tickets:
        for i, value in enumerate(ticket):
            for field_name, ranges in field_rules.items():
                valid_for_field = False
                for low, high in ranges:
                    if low <= value <= high:
                        valid_for_field = True
                        break
                if not valid_for_field:
                    possible_fields[i].discard(field_name)

    field_mapping = {}
    while len(field_mapping) < num_fields:
        for i in range(num_fields):
            if i in field_mapping:
                continue
            if len(possible_fields[i]) == 1:
                field_name = list(possible_fields[i])[0]
                field_mapping[i] = field_name
                for j in range(num_fields):
                    if j != i:
                        possible_fields[j].discard(field_name)

    answer = 1
    for i, field_name in field_mapping.items():
        if field_name.startswith("departure"):
            answer *= my_ticket[i]

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
