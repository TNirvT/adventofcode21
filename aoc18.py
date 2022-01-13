from math import ceil
from itertools import permutations
import re

REGULAR = re.compile(r"\d+,\d+")
REG_LEFT = re.compile(r"\d+")
REG_RIGHT = re.compile(r"(?<=,)\d+")

def open_file(filename) -> list[str]:
    with open(filename) as f:
        inputs = []
        for line in f:
            inputs.append(line.rstrip())
        return inputs

def add_sf(snailfish1: str, snailfish2: str) -> str:
    return f"[{snailfish1},{snailfish2}]"

def explode_sf(snailfish: str):
    i, nested = 0, 0
    for char in snailfish:
        if char == "[":
            nested += 1
            matched = REGULAR.match(snailfish[i+1:])
            if nested > 4 and matched:
                result_left = ""
                left_match = re.search(r"\d+", snailfish[i::-1])
                if left_match:
                    left_span = i + 1 - left_match.span()[1], i - left_match.span()[0]
                    new_left = int(left_match[0][::-1]) + int(REG_LEFT.match(matched[0])[0])
                    result_left = snailfish[:left_span[0]] + str(new_left) + snailfish[left_span[1] + 1:i] + "0"

                right_match = re.search(r"\d+", snailfish[i + 2 + matched.span()[1]:])
                if right_match:
                    right_span = i + 2 + matched.span()[1] + right_match.span()[0], i + 1 + matched.span()[1] + right_match.span()[1]
                    new_right = int(right_match[0]) + int(REG_RIGHT.search(matched[0])[0])
                    result_right = snailfish[i + 2 + matched.span()[1]:i + 2 + matched.span()[1] + right_match.span()[0]] + str(new_right) + re.search(r"(?<=\d)\D+.+", snailfish[i + 2 + matched.span()[1]:])[0]
                    if result_left:
                        return result_left + result_right
                    else:
                        return snailfish[:i] + "0" + result_right
                else:
                    return result_left + re.search(r"(?<=]).+", snailfish[i:])[0]
        elif char == "]":
            nested += -1

        i += 1
    return

def split_sf(snailfish: str):
    split_match = re.search(r"\d{2,}", snailfish)
    if split_match:
        number = int(split_match[0])
        pair = f"[{number // 2},{ceil(number / 2)}]"
        return snailfish[:split_match.span()[0]] + pair + snailfish[split_match.span()[1]:]
    return

def reduce_sf(snailfish: str):
    while True:
        exploded = explode_sf(snailfish)
        splited = split_sf(snailfish)
        if exploded:
            snailfish = exploded
        elif splited:
            snailfish = splited
        else:
            break
    return snailfish

def magnitude_sf(snailfish: str):
    result_mag = snailfish
    while True:
        reg_match = REGULAR.search(result_mag)
        if reg_match:
            reg_span = reg_match.span()[0], reg_match.span()[1]
            mag = int(REG_LEFT.match(reg_match[0])[0]) * 3 + int(REG_RIGHT.search(reg_match[0])[0]) * 2
            result_mag = result_mag[:reg_span[0] - 1] + str(mag) + result_mag[reg_span[1] + 1:]
        else:
            return int(result_mag)


if __name__ == "__main__":
    # inputs = open_file("test.txt")
    inputs = open_file("aoc18.txt")

    result = ""
    for line in inputs:
        if not result:
            result = reduce_sf(line)
        else:
            result = reduce_sf(add_sf(result, line))
    print(result)
    print(f"Part one: {magnitude_sf(result)}")

    permute = permutations(inputs, 2)
    mag_list = []
    for pair in permute:
        sum_sf = reduce_sf(add_sf(pair[0], pair[1]))
        mag = magnitude_sf(sum_sf)
        mag_list.append(mag)
    print(f"Part two: {max(mag_list)}")
