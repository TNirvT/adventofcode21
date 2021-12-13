def open_file(filename: str) -> dict:
    with open(filename) as f:
        inputs = {"start": []}
        for line in f:
            nodes = line.rstrip().split("-", 1)
            for i in range(2):
                if nodes[i] == "end" or nodes[i-1] == "start":
                    pass
                elif nodes[i] != "start" and nodes[i] not in inputs:
                    inputs[nodes[i]] = [nodes[1-i]]
                elif nodes[i] != "start":
                    inputs[nodes[i]].append(nodes[1-i])
                else:
                    inputs["start"].append(nodes[1-i])
        ### Caution!!
        inputs_keys = list(inputs.keys())
        for node in inputs_keys:
            if node.islower() and len(inputs[node]) == 1 and inputs[node][0].islower():
                del inputs[node]
        ###
    return inputs

def all_paths_recur(caves: dict[str, list[str]], start: str, visited: dict[str, int], part: int):
    visited[start] += 1

    if start == "end":
        visited[start] += -1
        return 1
    elif start not in caves:
        print("node is not connected")

    count = 0
    for node in caves[start]:
        if visited[node] == 0 or node.isupper():
            count += all_paths_recur(caves, node, visited, part)
        elif part == 2 and visited[node] == 1:
            count += all_paths_recur(caves, node, visited, 1)
    visited[start] += -1
    return count

def all_paths(caves: dict[str, list[str]], part: int):
    visited = {k:0 for k in caves}
    visited["end"] = 0
    count = all_paths_recur(caves, "start", visited, part)
    return count

if __name__ == "__main__":
    inputs = open_file("aoc12.txt")
    # inputs = open_file("test.txt")
    print(inputs)
    count = all_paths(inputs, 1)
    print(f"Part one: {count}")
    count = all_paths(inputs, 2)
    print(f"Part two: {count}")
