with open("aoc10.txt", "r") as f:
# with open("test.txt", "r") as f:
    inputs = f.readlines()
    inputs = [x.rstrip() for x in inputs]

class Chunks:
    def __init__(self) -> None:
        self.top = None
        self.points = 0
        self.rules = {'(': ')', '[': ']', '{': '}', '<': '>'}
    
    class Node:
        def __init__(self, char, next) -> None:
            self.char = char
            self.next = next
    
    def add(self, char):
        ill_pts = {')': 3, ']': 57, '}': 1197, '>': 25137}
        if self.top != None and char == self.rules.get(self.top.char):
            self.top = self.top.next
        elif char in self.rules.keys():
            self.top = self.Node(char, self.top)
        elif char in self.rules.values():
            # print(f"corrupted, illegal close with: {char}, expected: {self.rules[self.top.char]}")
            self.points += ill_pts[char]
            raise AssertionError
        else:
            print("unknown input")
            raise TypeError

    def remove(self) -> str:
        if self.top != None:
            close_by = self.rules[self.top.char]
            self.top = self.top.next
            return close_by
        else:
            raise ValueError

def completing(chunk: Chunks) -> int:
    completion_pts = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    while chunk.top != None:
        score = score * 5 + completion_pts[chunk.remove()]
    return score

result = 0
scores = []
for line in inputs:
    chunk = Chunks()
    incomplete = True
    for char in line:
        try:
            chunk.add(char)
        except AssertionError:
            incomplete = False
            break
    result += chunk.points
    if incomplete:
        scores.append(completing(chunk))
print(f"Part one: {result}")

scores.sort()
print(f"Part two: {scores[(len(scores)//2)]}")
