import re

with open("aoc08.txt", "r") as f:
    inputs = f.readlines()
    inputs = [x.rstrip() for x in inputs]

inputs = [x.split(sep=" | ", maxsplit=1) for x in inputs]
# print(*inputs, sep="\n")

def count_unique(inputs: list[list[str]]) -> int:
    total = 0
    for entry in inputs:
        tmp = [len(x) for x in entry[1].split()]
        total += tmp.count(2) + tmp.count(3) + tmp.count(4) + tmp.count(7)
    return total

print(f"Part one: Total= {count_unique(inputs)}")

def decode(codes: list[str]) -> dict:
    decoded = {}
    two_three_five = []
    zero_six_nine = []
    for code_str in codes:
        if len(code_str) == 2:
            code_str_1 = code_str
            decoded["".join(sorted(code_str))] = "1"
        elif len(code_str) == 4:
            code_str_4 = code_str
            decoded["".join(sorted(code_str))] = "4"
        elif len(code_str) == 3:
            decoded["".join(sorted(code_str))] = "7"
        elif len(code_str) == 7:
            decoded["".join(sorted(code_str))] = "8"
        elif len(code_str) == 5:
            two_three_five.append(code_str)
        else:
            zero_six_nine.append(code_str)

    if len(two_three_five) != 3 or len(zero_six_nine) != 3:
        print(f"Incorrect '235'({two_three_five} / '069'({zero_six_nine}))")
        raise AssertionError

    adg = ''.join(set(two_three_five[0]).intersection(two_three_five[1]).intersection(two_three_five[2]))
    # print(f"adg: {adg}")
    code_str_3 = code_str_1 + adg
    decoded["".join(sorted(code_str_3))] = "3"

    bd = re.sub('[' + code_str_1 + ']', '', code_str_4)
    # print(f"bd: {bd}")
    for code_str in two_three_five:
        if set(bd).issubset(set(code_str)):
            decoded["".join(sorted(code_str))] = "5"
        elif set(code_str) != set(code_str_3):
            decoded["".join(sorted(code_str))] = "2"
    
    d = ''.join(set(adg).intersection(bd))
    for code_str in zero_six_nine:
        if d not in code_str:
            decoded["".join(sorted(code_str))] = "0"
        elif set(code_str_1).issubset(set(code_str)):
            decoded["".join(sorted(code_str))] = "9"
        else:
            decoded["".join(sorted(code_str))] = "6"

    return decoded

results = []
for line in inputs:
    decoded = decode(line[0].split())
    result = ""
    for code_str in line[1].split():
        result += decoded["".join(sorted(code_str))]
    results.append(int(result))

print(f"Part two: Total= {sum(results)}")
