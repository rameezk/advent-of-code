from aoc.helper import AOC
import re


@AOC.puzzle(2016, 7, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """aba[bab]xyz
# xyx[xyx]xyx
# aaa[kek]eke
# zazbz[bzb]cdb""".strip().splitlines()

    def find_aba_patterns(s):
        patterns = []
        for i in range(len(s) - 2):
            if s[i] == s[i+2] and s[i] != s[i+1]:
                patterns.append(s[i:i+3])
        return patterns

    def aba_to_bab(aba):
        return aba[1] + aba[0] + aba[1]

    def supports_ssl(ip):
        hypernet_sequences = re.findall(r'\[([^\]]+)\]', ip)
        supernet_sequences = re.split(r'\[[^\]]+\]', ip)

        supernet_abas = []
        for supernet in supernet_sequences:
            supernet_abas.extend(find_aba_patterns(supernet))

        hypernet_babs = []
        for hypernet in hypernet_sequences:
            hypernet_babs.extend(find_aba_patterns(hypernet))

        for aba in supernet_abas:
            bab = aba_to_bab(aba)
            if bab in hypernet_babs:
                return True

        return False

    count = sum(1 for ip in data if supports_ssl(ip))

    print(count)
    AOC.submit_answer(count)


if __name__ == "__main__":
    solve()
