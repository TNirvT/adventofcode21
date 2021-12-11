from copy import deepcopy

with open("aoc09.txt", "r") as f:
# with open("test.txt", "r") as f:
    inputs = f.readlines()
    inputs = [x.rstrip() for x in inputs]

class HMap:
    def __init__(self) -> None:
        self.rowSize = 0
        self.columnSize = 0
        self.top = self.bottom = None
    
    class Row:
        def __init__(self, data, up, down) -> None:
            self.data = data
            self.up = up
            self.down = down
    
    # always add row to the bottom
    def add(self, string: str):
        if self.columnSize == 0:
            self.columnSize = len(string)
        elif self.columnSize != len(string):
            print(f"input string must be same length ({self.columnSize})")
            raise ValueError
        
        if self.rowSize == 0:
            self.top = self.bottom = self.Row(string, None, None)
        else:
            self.bottom.down = self.Row(string, self.bottom, None)
            self.bottom = self.bottom.down
        self.rowSize += 1

    def cursor_factory(self):
        return HMap.Cursor(self)

    class Cursor:
        def __init__(self, hmap_instance) -> None:
            self.hmap_instance = hmap_instance
            self.row = hmap_instance.top
            self.row_index = 0
            self.column = 0

        def value(self):
            return int(self.row.data[self.column])

        def forward(self):
            if self.column != self.hmap_instance.columnSize - 1:
                self.column += 1
            else:
                self.row = self.row.down
                self.row_index += 1
                self.column = 0

        def backward(self):
            if self.column != 0:
                self.column += -1
            else:
                self.row = self.row.up
                self.row_index += -1
                self.column = self.hmap_instance.columnSize - 1

        def upward(self):
            if self.row_index != 0:
                self.row_index += -1
                self.row = self.row.up
            else:
                raise IndexError
        
        def downward(self):
            if self.row_index != self.hmap_instance.rowSize - 1:
                self.row_index += 1
                self.row = self.row.down
            else:
                raise IndexError

        def up(self):
            if self.row.up:
                return int(self.row.up.data[self.column])
            else:
                return None

        def down(self):
            if self.row.down:
                return int(self.row.down.data[self.column])
            else:
                return None

        def left(self):
            if self.column != 0:
                return int(self.row.data[self.column - 1])
            else:
                return None

        def right(self):
            if self.column != self.hmap_instance.columnSize - 1:
                return int(self.row.data[self.column + 1])
            else:
                return None

def low_pt(cursor: HMap.Cursor) -> bool:
    det = []
    cursor.up() != None and det.append(cursor.up() > cursor.value())
    cursor.down() != None and det.append(cursor.down() > cursor.value())
    cursor.left() != None and det.append(cursor.left() > cursor.value())
    cursor.right() != None and det.append(cursor.right() > cursor.value())
    if all(det):
        return True
    else:
        return False

hmap = HMap()
for data in inputs:
    hmap.add(data)
cursor = hmap.cursor_factory()

# rowCursor = hmap.top
# for i in range(hmap.rowSize):
#     print(rowCursor.data)
#     rowCursor = rowCursor.down

result = 0
for _ in range(hmap.rowSize * hmap.columnSize):
    if low_pt(cursor):
        # print(cursor.value())
        result += cursor.value() + 1
    cursor.forward()

print(f"Part one: {result}")

cursor = hmap.cursor_factory()
basin = {}
for _ in range(hmap.rowSize * hmap.columnSize):
    # print(f"v: {cursor.value()}")
    if cursor.value() == 9:
        pass
    elif low_pt(cursor):
        if basin.get((cursor.row_index, cursor.column)):
            basin[cursor.row_index, cursor.column] += 1
        else:
            basin[cursor.row_index, cursor.column] = 1
        # print(basin)
    else:
        to_low_pt = deepcopy(cursor)
        while not low_pt(to_low_pt):
            if to_low_pt.up() != None and to_low_pt.up() < to_low_pt.value():
                to_low_pt.upward()
            elif to_low_pt.down() != None and to_low_pt.down() < to_low_pt.value():
                to_low_pt.downward()
            elif to_low_pt.left() != None and to_low_pt.left() < to_low_pt.value():
                to_low_pt.backward()
            elif to_low_pt.right() != None and to_low_pt.right() < to_low_pt.value():
                to_low_pt.forward()
        if basin.get((to_low_pt.row_index, to_low_pt.column)):
            # print(basin)
            basin[to_low_pt.row_index, to_low_pt.column] += 1
        else:
            basin[to_low_pt.row_index, to_low_pt.column] = 1
        # print(basin)
    cursor.forward()

result = 1
for i in [sorted(list(basin.values()), reverse=True)[x] for x in range(3)]:
    result *= i
print(f"Part two: {result}")
