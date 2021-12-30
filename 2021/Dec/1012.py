def dfs(board, y, x, m, n):
    stack = []
    visited = []
    stack.append((x, y))
    grid_x = [-1, 1, 0, 0]
    grid_y = [0, 0, -1, 1]
    while stack:
        _x, _y = stack.pop()
        if (_x, _y) not in visited:
            board[_y][_x] = 0
            visited.append((_x, _y))
            for g_x, g_y in zip(grid_x, grid_y):
                dx = _x + g_x
                dy = _y + g_y
                if m > dx >= 0 and n > dy >= 0 and board[dy][dx]:
                    stack.append((dx, dy))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for a in range(m)] for b in range(n)]
    for c in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                dfs(board, i, j, m, n)
                cnt += 1
    print(cnt)


