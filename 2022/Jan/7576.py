def check_full(board):
    global n, m
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                return 0
    return 1


m, n = map(int, input().split())
board = []
def bfs(x, y):
    


for i in range(n):
    board.append(list(map(int, input().split())))
while not check_full(board):
    visited = [[0 for i in range(n)] for j in range(m)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == -1:



