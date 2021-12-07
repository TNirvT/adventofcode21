with open("aoc07.txt", "r") as f:
    positions = f.readline().split(sep=",")
    positions = [int(x) for x in positions]
# positions = [16,1,2,0,4,2,7,1,2,14]

def to_dct(positions: list) -> dict:
    mx = max(positions)
    positions_dct = {}
    for i in range(mx + 1):
        positions_dct[i] = positions.count(i)
    return positions_dct

positions_dct = to_dct(positions)
# print(positions_dct)
results = []
for align_at in range(len(positions)):
    energy = 0
    for j in positions_dct:
        energy += abs(j - align_at) * positions_dct[j]
    results.append(energy)
# print(results)
print("***Part one***")
print(f"Min position: {results.index(min(results))}")
print(f"with engery: {min(results)}")

results = []
for align_at in range(len(positions)):
    energy = 0
    for j in positions_dct:
        steps = abs(j - align_at)
        energy += (1 + steps) * (steps /2) * positions_dct[j]
    results.append(energy)

print("***Part two***")
print(f"Min position: {results.index(min(results))}")
print(f"with engery: {min(results)}")
