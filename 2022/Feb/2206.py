import sys
import collections

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input().rstrip()))


def bfs():
    global n, m
    queue = collections.deque()
    queue.append((0, 0, 1, False))
    visited = [[[False] * 2 for a in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    deg_x = [-1, 1, 0, 0]
    deg_y = [0, 0, -1, 1]
    while queue:
        x, y, cnt, break_flag = queue.popleft()
        if x == n - 1 and y == m - 1:
            print(cnt)
            return
        for dx, dy in zip(deg_x, deg_y):
            lx, ly = x + dx, y + dy
            if 0 <= lx < n and 0 <= ly < m:
                if board[lx][ly] == '0':
                    if not break_flag and not visited[lx][ly][break_flag]:
                        queue.append((lx, ly, cnt + 1, break_flag))
                        visited[lx][ly][break_flag] = True
                    elif break_flag and not visited[lx][ly][break_flag] and not visited[lx][ly][False]:
                        queue.append((lx, ly, cnt + 1, break_flag))
                        visited[lx][ly][break_flag] = True
                elif board[lx][ly] == '1' and not visited[lx][ly][1] and not break_flag:
                    queue.append((lx, ly, cnt + 1, True))
                    visited[lx][ly][1] = True
    print(-1)
    return


bfs()