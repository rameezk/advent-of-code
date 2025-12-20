from aoc.helper import AOC

@AOC.puzzle(2020, 4, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
# byr:1937 iyr:2017 cid:147 hgt:183cm
#
# iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
# hcl:#cfa07d byr:1929
#
# hcl:#ae17e1 iyr:2013
# eyr:2024
# ecl:brn pid:760753108 byr:1931
# hgt:179cm
#
# hcl:#cfa07d eyr:2025 pid:166559648
# iyr:2011 ecl:brn hgt:59in"""

    passports = data.split("\n\n")

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    valid_count = 0
    for passport in passports:
        fields = {}
        tokens = passport.replace("\n", " ").split()
        for token in tokens:
            key, value = token.split(":")
            fields[key] = value

        if required_fields.issubset(fields.keys()):
            valid_count += 1

    answer = valid_count
    print(f"Part 1: {answer}")
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
