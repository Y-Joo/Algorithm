def dfs(board, x, y, m, n):
    stack = []
    visited = []
    stack.append((x, y))
    grid_x = [-1, 1]
    grid_y = [-1, 1]
    while stack:
        _x, _y = stack.pop()
        print(_x, _y)
        if (_x, _y) not in visited:
            board[_x][_y] = 0
            visited.append((_x, _y))
            for g_x in grid_x:
                for g_y in grid_y:
                    dx = _x + g_x
                    dy = _y + g_y
                    if m > dx >= 0 and n > dy >= 0 and board[dx][dy]:
                        stack.append((dx, dy))

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for a in range(m)] for b in range(n)]
    for c in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    cnt = 0
    for k in range(n):
        print(board[k])
    print("-------------------")
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                dfs(board, i, j, m, n)
                for k in range(n):
                    print(board[k])
                print("-------------------")
                cnt += 1
    print(cnt)


