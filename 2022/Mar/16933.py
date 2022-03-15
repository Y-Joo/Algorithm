import collections
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, list(input().rstrip()))))
visited = [[-1] * m for a in range(n)]


def bfs():
    global n, m, k
    queue = collections.deque()
    queue.append((0, 0, k, 1, 1))
    grid_x = [-1, 1, 0, 0]
    grid_y = [0, 0, -1, 1]
    visited[0][0] = k
    while queue:
        x, y, break_cnt, cnt, day_flag = queue.popleft()
        if x == n - 1 and y == m - 1:
            print(cnt)
            return
        for dx, dy in zip(grid_x, grid_y):
            lx, ly = x + dx, y + dy
            if 0 <= lx < n and 0 <= ly < m:
                if board[lx][ly] == 0:
                    if visited[lx][ly] < break_cnt:
                        queue.append((lx, ly, break_cnt, cnt + 1, -day_flag))
                        visited[lx][ly] = break_cnt
                elif break_cnt > 0:
                    if visited[lx][ly] < break_cnt - 1:
                        if day_flag == 1:
                            queue.append((lx, ly, break_cnt - 1, cnt + 1, -day_flag))
                            visited[lx][ly] = break_cnt - 1
                        elif day_flag == -1:
                            queue.append((x, y, break_cnt, cnt + 1, -day_flag))
    print(-1)


bfs()