def open_file(file_name: str):
    with open(file_name, "r") as f:
        inputs = []
        instructions = []
        for line in f:
            if line == "\n":
                pass
            elif "fold along" not in line:
                inputs.append(tuple(line.rstrip().split(",")))
            else:
                instructions.append(line.rstrip().split("="))

    inputs = [(int(i),int(j)) for i, j in inputs]
    instructions = [(x[0][-1], int(x[1])) for x in instructions]
    print(inputs, "\n", instructions)
    return inputs, instructions

def page_initialization(inputs):
    page = [[False]*(max(x[0] for x in inputs) + 1) for _ in range(max(x[1] for x in inputs) + 1)]
    print(f"Original Page size: {len(page[0])} cols x {len(page)} rows")
    for dot in inputs:
        page[dot[1]][dot[0]] = True
    # print(*page, sep="\n")
    return page

def fold(page: list[list[int]], along: tuple[str, int]):
    if along[0] == "y":
        m = along[1]
        n = len(page[0])
        new_page = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_page[i][j] = page[i][j] or (2*m - i < len(page) and page[2*m - i][j])
    else: # along[0] == "x"
        m = len(page)
        n = along[1]
        new_page = [[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_page[i][j] = page[i][j] or (2*n - j < len(page[0]) and page[i][2*n - j])
    return new_page

def count(page: list[list[bool]]) -> int:
    count = 0
    for i in range(len(page)):
        for j in range(len(page[0])):
            if page[i][j]:
                count += 1
    return count

def translate(line: list) -> str:
    translated = ["#" if x else " " for x in line]
    return "".join(translated)

if __name__ == "__main__":
    # inputs, instructions = open_file("test.txt")
    inputs, instructions = open_file("aoc13.txt")
    page = page_initialization(inputs)
    # print(*page, sep="\n")
    new_page = fold(page, instructions[0])
    print(f"Part one: {count(new_page)}")

    for i in range(1, len(instructions)):
        new_page = fold(new_page, instructions[i])
    for line in new_page:
        print(translate(line))
