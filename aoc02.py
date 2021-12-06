position, depth = 0, 0
inputs= []

with open("aoc02.txt") as f:
    inputs = f.readlines()

for i in range(len(inputs)):
    inputs[i] = inputs[i].rstrip().split(" ")
    inputs[i][1] = int(inputs[i][1])

print(len(inputs))

def move(command: list[str, int]) -> None:
    global position, depth
    match command[0]:
        case "forward":
            position += command[1]
        case "down":
            depth += command[1]
        case "up":
            depth -= command[1]
        case _:
            raise KeyError

for command in inputs:
    move(command)
print(f"multiply result: {position * depth}")

def newMove(command: list[str, int]) -> None:
    global position, depth, aim
    match command[0]:
        case "forward":
            position += command[1]
            depth += aim * command[1]
        case "down":
            aim += command[1]
        case "up":
            aim -= command[1]
        case _:
            raise KeyError

position, depth, aim = 0, 0, 0

for command in inputs:
    newMove(command)
print(f"new multiply result: {position * depth}")
