import sys
import collections
input = sys.stdin.readline
def check_full(board):
    global n, m
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                return 0
    return 1


m, n = map(int, input().split())
board = []
queue = collections.deque([])
for i in range(n):
    board.append(list(map(int, input().split())))
    for j in range(m):
        if board[i][j] == 1:
            queue.append((i, j))


def bfs():
    grid_x = [-1, 1, 0, 0]
    grid_y = [0, 0, -1, 1]
    while queue:
        y, x = queue.popleft()
        for dx, dy in zip(grid_x, grid_y):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < m and 0 <= ny < n and not board[ny][nx]:
                queue.append((ny, nx))
                board[ny][nx] = board[y][x] + 1


bfs()
ans = 0
for i in board:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    ans = max(ans, max(i))
print(ans - 1)


