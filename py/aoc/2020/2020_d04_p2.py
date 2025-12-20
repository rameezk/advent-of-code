import re
from aoc.helper import AOC

@AOC.puzzle(2020, 4, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """eyr:1972 cid:100
# hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
# iyr:2019
# hcl:#602927 eyr:1967 hgt:170cm
# ecl:grn pid:012533040 byr:1946
#
# hcl:dab227 iyr:2012
# ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
# hgt:59cm ecl:zzz
# eyr:2038 hcl:74454a iyr:2023
# pid:3556412378 byr:2007
#
# pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
# hcl:#623a2f
#
# eyr:2029 ecl:blu cid:129 byr:1989
# iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
#
# hcl:#888785
# hgt:164cm byr:2001 iyr:2015 cid:88
# pid:545766238 ecl:hzl
# eyr:2022
#
# iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

    passports = data.split("\n\n")

    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    def validate_byr(value):
        if len(value) == 4 and value.isdigit():
            year = int(value)
            return 1920 <= year <= 2002
        return False

    def validate_iyr(value):
        if len(value) == 4 and value.isdigit():
            year = int(value)
            return 2010 <= year <= 2020
        return False

    def validate_eyr(value):
        if len(value) == 4 and value.isdigit():
            year = int(value)
            return 2020 <= year <= 2030
        return False

    def validate_hgt(value):
        match = re.match(r'^(\d+)(cm|in)$', value)
        if match:
            height = int(match.group(1))
            unit = match.group(2)
            if unit == 'cm':
                return 150 <= height <= 193
            elif unit == 'in':
                return 59 <= height <= 76
        return False

    def validate_hcl(value):
        return bool(re.match(r'^#[0-9a-f]{6}$', value))

    def validate_ecl(value):
        return value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    def validate_pid(value):
        return bool(re.match(r'^\d{9}$', value))

    validators = {
        'byr': validate_byr,
        'iyr': validate_iyr,
        'eyr': validate_eyr,
        'hgt': validate_hgt,
        'hcl': validate_hcl,
        'ecl': validate_ecl,
        'pid': validate_pid,
    }

    valid_count = 0
    for passport in passports:
        fields = {}
        tokens = passport.replace("\n", " ").split()
        for token in tokens:
            key, value = token.split(":")
            fields[key] = value

        if required_fields.issubset(fields.keys()):
            all_valid = True
            for field_name in required_fields:
                if not validators[field_name](fields[field_name]):
                    all_valid = False
                    break
            if all_valid:
                valid_count += 1

    answer = valid_count
    print(f"Part 2: {answer}")
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
