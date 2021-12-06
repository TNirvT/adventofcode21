inputs = []
count = 0

with open("aoc01.txt") as f:
    inputs = f.readlines()
    inputs = [int(line.rstrip()) for line in inputs]

print(f"total inputs: {len(inputs)}")
# print(inputs)

for i in range(len(inputs) - 1):
    if inputs[i+1] > inputs[i]:
        count += 1

print(f"counted: {count}")

newCount = 0

for i in range(len(inputs) - 3):
    if inputs[i+3] > inputs[i]:
        newCount += 1

print(f"new counted: {newCount}")
