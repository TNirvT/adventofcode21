diagram = [[0] *1000 for _ in range(1000) ]
# print(*diagram, sep="\n")

with open("aoc05.txt", "r") as f:
    vents = f.readlines()
    vents = [points.rstrip().split(sep=" -> ") for points in vents]
for points in vents:
    points[0] = int(points[0].split(sep=",")[0]), int(points[0].split(sep=",")[1])
    points[1] = int(points[1].split(sep=",")[0]), int(points[1].split(sep=",")[1])
# print(vents)

def draw(diagram):
    for points in vents:
        point0, point1 = points[0], points[1]
        if point0[0] == point1[0]:
            distance = point1[1] - point0[1]
            step = 1 if distance > 0 else -1
            for i in range(abs(distance) + 1):
                diagram[point0[1] + i*step][point0[0]] += 1
        elif point0[1] == point1[1]:
            distance = point1[0] - point0[0]
            step = 1 if distance > 0 else -1
            for i in range(abs(distance) + 1):
                diagram[point0[1]][point0[0] + i*step] += 1
    return diagram

def draw_diagonal(diagram):
    for points in vents:
        point0, point1 = points[0], points[1]
        if point1[0] - point0[0] == point1[1] - point0[1]:
            step = 1 if point1[0] - point0[0] > 0 else -1
            for i in range(abs(point1[0] - point0[0]) +1):
                diagram[point0[1] + i*step][point0[0] + i*step] += 1
        if point1[0] - point0[0] == point0[1] - point1[1]:
            step = 1 if point1[0] - point0[0] > 0 else -1
            for i in range(abs(point1[0] - point0[0]) +1):
                diagram[point0[1] - i*step][point0[0] + i*step] += 1
    return diagram

new_diagram = draw(diagram)
# print(*new_diagram, sep="\n")
count = 0
for row in new_diagram:
    count += sum(map(lambda x: x > 1, row))
print(f"count: {count}")

new_diagram = draw_diagonal(new_diagram)
# print(*new_diagram, sep="\n")
count = 0
for row in new_diagram:
    count += sum(map(lambda x: x > 1, row))
print(f"count2: {count}")
