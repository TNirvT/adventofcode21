with open("aoc04.txt", "r") as f:
    draws = f.readline().rstrip()
    draws = [int(x) for x in draws.split(sep=",")]
    boards = []
    while True:
        lead_space = f.readline()
        if lead_space.isspace():
            board = []
            for _ in range(5):
                line = f.readline().strip()
                line = [int(x) for x in line.split()]
                for entry in line:
                    board.append(entry)
            if len(board) != 25:
                print("Error. Board is not 5x5")
                raise ValueError
            boards.append(board)
        elif not lead_space:
            break
        else:
            print("Error reading leading space line")
            raise TypeError

print(f"There are {len(boards)} boards.")

games = []
for _ in range(len(boards)):
    game = {}
    for i in range(5*5):
        game[i] = False
    games.append(game)

def wins(game: dict) -> bool:
    for i in range(5):
        row = []
        for j in range(5):
            row.append(game[5*i + j])
        if all(row):
            return True
    for k in range(5):
        column = []
        for l in range(5):
            column.append(game[k + 5*l])
        if all(column):
            return True
    return False

def sum_unmarked(i) -> int:
    result = 0
    for position in games[i]:
        if not games[i][position]:
            result += boards[i][position]
    return result

def part1():
    for draw in draws:
        for i in range(len(boards)):
            try:
                position = boards[i].index(draw)
                games[i][position] = True
                if wins(games[i]):
                    print(f"draw: {draw}")
                    print(f"Board no.{i} wins!")
                    print(f"umarked: {sum_unmarked(i)}")
                    print(f"score: {draw * sum_unmarked(i)}")
                    return
            except ValueError:
                pass

def part2():
    boards_left = list(range(len(boards)))
    for draw in draws:
        for i in range(len(boards)):
            try:
                position = boards[i].index(draw)
                games[i][position] = True
                if wins(games[i]):
                    try:
                        boards_left.remove(i)
                        if len(boards_left) == 0:
                            print(f"draw: {draw}")
                            print(f"score: {draw * sum_unmarked(i)}")
                            return
                    except ValueError:
                        pass
            except ValueError:
                pass

part2()
