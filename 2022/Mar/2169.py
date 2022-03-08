import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
dp = [[[-200000000] * 3 for i in range(m)] for _ in range(n)]
grid_x = [0, 1, 0]
grid_y = [-1, 0, 1]
for i in range(3):
    dp[0][0][i] = board[0][0]
for i in range(n):
    for j in range(m):
        if j > 0:
            dp[i][j][0] = max(dp[i][j][0], dp[i][j - 1][0] + board[i][j], dp[i][j - 1][1] + board[i][j])
        if i > 0:
            dp[i][j][1] = max(dp[i][j][1], dp[i - 1][j][0] + board[i][j], dp[i - 1][j][1] + board[i][j], dp[i - 1][j][2] + board[i][j])
    for j in range(m - 1, -1, -1):
        if j < m - 1:
            dp[i][j][2] = max(dp[i][j][2], dp[i][j + 1][1] + board[i][j], dp[i][j + 1][2] + board[i][j])


print(max(dp[n - 1][m - 1]))
