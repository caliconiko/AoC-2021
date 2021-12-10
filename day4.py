import numpy as np

with open("day4.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in f.readlines()]


doub = raw.split("\n\n")
def part1():
    boards = [[[int(n) for n in l.split()] for l in b.split("\n")] for b in doub[1:] ]
    boards_np = np.array(boards)
    nums = [int(d) for d in doub[0].split(",")]
    empty_boards = [[[-1 for n in l.split()] for l in b.split("\n")] for b in doub[1:] ]
    empty_boards_np = np.array(empty_boards)

    def check_bingo(b):
        for i in range(5):
            if np.all(b[i] != -1):
                return True
            col = np.array([l[i] for l in b])
            if np.all(col != -1):
                return True

        return False

    for n in nums:
        empty_boards_np[np.where(boards_np==n)]=1
        for i, eb  in enumerate(empty_boards_np):
            if check_bingo(eb):
                return np.sum(boards_np[i][np.where(eb==-1)])*n

    return boards

def part2():
    boards = [[[int(n) for n in l.split()] for l in b.split("\n")] for b in doub[1:] ]
    boards_np = np.array(boards)
    nums = [int(d) for d in doub[0].split(",")]
    empty_boards = [[[-1 for n in l.split()] for l in b.split("\n")] for b in doub[1:] ]
    empty_boards_np = np.array(empty_boards)

    def check_bingo(b):
        for i in range(5):
            if np.all(b[i] != -1):
                return True
            col = np.array([l[i] for l in b])
            if np.all(col != -1):
                return True

        return False

    all_wins = []
    all_win_nums =[]
    all_win_boards =[]
    for n in nums:
        empty_boards_np[np.where(boards_np==n)]=1
        wins = []
        for i, eb  in enumerate(empty_boards_np):
            if check_bingo(eb):
                wins.append(i)
        all_wins.append(wins)
        all_win_nums.append(n)
        all_win_boards.append(empty_boards_np.copy())

    final = None
    fin_num = None
    fin_board = None
    for i, wins in enumerate(all_wins[::-1]):
        print(f"{all_wins[::-1][i]} {wins}")
        if wins != all_wins[::-1][i+1]:
            final =  list(set(wins)-set(all_wins[::-1][i+1]))[0]
            fin_num = all_win_nums[::-1][i]
            fin_board = all_win_boards[::-1][i]
            break

    return np.sum(boards_np[final][np.where(fin_board[final]==-1)])*fin_num

print(part2())
