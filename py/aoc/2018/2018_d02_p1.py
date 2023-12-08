from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2018, 2)

    with open("./2018_d02.txt") as f:
        data = f.read().strip().splitlines()

    # data = [
    #     "abcdef",
    #     "bababc",
    #     "abbcde",
    #     "abcccd",
    #     "aabcdd",
    #     "abcdee",
    #     "ababab",
    # ]

    appears_twice_count = 0
    appears_thrice_count = 0
    for line in data:
        unique_characters = set(line)

        found_twice = False
        found_thrice = False

        for char in sorted(unique_characters):
            count = line.count(char)
            if count == 2:
                found_twice = True
            if count == 3:
                found_thrice = True

            if found_twice and found_thrice:
                break

        if found_twice:
            appears_twice_count += 1

        if found_thrice:
            appears_thrice_count += 1

    checksum = appears_twice_count * appears_thrice_count
    print(checksum)

    # submit_answer(2018, 2, 1, checksum)
