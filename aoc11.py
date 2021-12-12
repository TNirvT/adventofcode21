from itertools import product

with open("aoc11.txt", "r") as f:
# with open("test.txt", "r") as f:
    inputs = []
    for line in f:
        inputs.append([int(i) for i in list(line.rstrip())])

def start(arr: list[list[int]]):
    length = len(arr[0])
    for row in arr:
        for i in range(length):
            row[i] += 1

def more_flash(arr: list[list[int]], flashed: list[list[int]]) -> bool:
    no_of_rows = len(arr)
    no_of_cols = len(arr[0])
    for i, j in product(range(no_of_rows), range(no_of_cols)):
        if arr[i][j] > 9 and not flashed[i][j]:
            return True
    return False

def flash(arr: list[list[int]]):
    no_of_rows = len(arr)
    no_of_cols = len(arr[0])
    flashed = [[0] * no_of_cols for _ in range(no_of_rows)]
    while more_flash(arr, flashed):
        for i, j in product(range(no_of_rows), range(no_of_cols)):
            if arr[i][j] > 9 and not flashed[i][j]:
                x, y = [i], [j]
                i != 0 and x.append(i-1)
                i != no_of_rows - 1 and x.append(i+1)
                j != 0 and y.append(j-1)
                j != no_of_cols - 1 and y.append(j+1)
                itr = list(product(x, y))
                itr.remove((i, j))
                for di, dj in itr:
                    arr[di][dj] += 1
                flashed[i][j] = 1
    for i, j in product(range(no_of_rows), range(no_of_cols)):
        if flashed[i][j]:
            arr[i][j] = 0
    no_of_flashes = 0
    for i in range(no_of_rows):
        no_of_flashes += sum(flashed[i])
    return no_of_flashes

print(*inputs, sep="\n")

n = 100

result = 0
for i in range(n):
    start(inputs)
    result += flash(inputs)
print(f"Part one: {result}")

no_of_step = 100
while True:
    start(inputs)
    flashing = flash(inputs)
    no_of_step += 1
    if flashing == len(inputs) * len(inputs[0]):
        print(f"Part two: {no_of_step}")
        break
