import re

def open_file(file_name: str):
    with open(file_name, "r") as f:
        start = f.readline().rstrip()
        inputs = []
        for line in f:
            if line == "\n":
                pass
            else:
                inputs.append(tuple(line.rstrip().split(" -> ")))

    return start, inputs

def compile_all(inputs: list[tuple[str, str]]):
    rules = []
    for rule in inputs:
        rules.append((re.compile(rule[0]), rule[1]))
    return rules

def find_all(start: str, pattern: re.Pattern):
    m = pattern.search(start)
    positions = []
    chopped = 0
    while m:
        if m:
            positions += [m.start() + chopped]
            chopped += m.start() + 1
            m = pattern.search(start[chopped:])
    return positions

def insert(start: str, rules: list[tuple[re.Pattern, str]]):
    insertions = {}
    for rule in rules:
        positions = find_all(start, rule[0])
        for position in positions:
            insertions[position] = rule[1]
    insert_at = list(insertions.keys())
    insert_at.sort()
    result = ""
    for i in range(len(insert_at)):
        j = 0 if i == 0 else insert_at[i-1] +1
        tail = start[insert_at[i] +1:] if i == len(insert_at) -1 else ""
        result += start[j :insert_at[i] +1] + insertions[insert_at[i]] + tail
    return result

def repeat(n, start, rules):
    for i in range(n):
        start = insert(start, rules)
    # print(start)
    char_set = set(start)
    char_counts = {}
    for char in char_set:
        char_counts[char] = start.count(char)
    values = char_counts.values()
    return max(values) - min(values)

def increment(d: dict, k: str, v):
    if k in d:
        d[k] += v
    else:
        d[k] = v

def insert_dict(polymer: dict, counts: dict, inputs: list[tuple[str, str]]):
    added = {}
    for rule in inputs:
        occur = polymer.get(rule[0])
        if occur:
            polymer[rule[0]] = 0
            increment(added, rule[0][0] + rule[1], occur)
            increment(added, rule[1] + rule[0][1], occur)
            increment(counts, rule[1], occur)
    for unit in added:
        increment(polymer, unit, added[unit])

def polymer_to_dict(start: str):
    polymer = {}
    counts = {}
    for i in range(len(start)-1):
        if start[i:i+2] in polymer:
            polymer[start[i:i+2]] += 1
        else:
            polymer[start[i:i+2]] = 1
        
    for char in set(start):
        counts[char] = start.count(char)
    return polymer, counts

if __name__ == "__main__":
    # start, inputs = open_file("test.txt")
    start, inputs = open_file("aoc14.txt")
    rules = compile_all(inputs)

    print(f"Part one: {repeat(10, start, rules)}")

    polymer, counts = polymer_to_dict(start)
    for _ in range(40):
        insert_dict(polymer, counts, inputs)
    print(f"Part two: {max(counts.values()) - min(counts.values())}")
