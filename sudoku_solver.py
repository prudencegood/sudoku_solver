board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def show(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j % 3 == 00 and j != 0:
                print('|', end=' ')
            print(board[i][j], end=' ')
        if i == 2 or i == 5:
            print("")
            print("---------------------", end="")

        print(" ")


def valid(num, row, column):
    global board
    # row
    for j in range(9):
        if board[row][j] == num and j != column:
            return False
    # column checking
    for i in range(9):
        if board[i][column] == num and i != row:
            return False
    # boxes checking
    x = row // 3
    y = column // 3
    for i in range(x * 3, (x * 3) + 3):
        for j in range(y * 3, (y * 3) + 3):
            if board[i][j] == num and (i, j) != (row, column):
                return False
    return True


def solve():
    global board
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for k in range(1, 10):
                    if valid(k, x, y):
                        board[x][y] = k
                        solve()
                        board[x][y] = 0
                return

    show(board)


solve()