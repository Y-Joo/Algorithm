import collections
import sys

input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    board = []
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y):
        cnt = 1
        board[x][y] = 0
        stack = [(x, y)]
        grid_x = [-1, 1, 0, 0]
        grid_y = [0, 0, -1, 1]
        visited[x][y] = True
        sector = [(x, y)]
        while stack:
            i, j = stack.pop()
            for dx, dy in zip(grid_x, grid_y):
                lx, ly = i + dx, j + dy
                if 0 <= lx < n and 0 <= ly < m:
                    if not board[lx][ly] and not visited[lx][ly]:
                        visited[lx][ly] = True
                        cnt += 1
                        stack.append((lx, ly))
                        sector.append((lx, ly))
        return cnt, sector

    lens = [[(0, -1)] * m for _ in range(n)]
    for _ in range(n):
        board.append(list(map(int, (list(input().rstrip())))))
    k = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0 and not visited[i][j]:
                cnt, sector = dfs(i, j)
                while sector:
                    x, y = sector.pop()
                    lens[x][y] = (cnt, k)
                k += 1
    grid_x = [-1, 1, 0, 0]
    grid_y = [0, 0, -1, 1]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                visited_sector = set()
                for dx, dy in zip(grid_x, grid_y):
                    lx, ly = i + dx, j + dy
                    if 0 <= lx < n and 0 <= ly < m:
                        if not board[lx][ly] and lens[lx][ly][1] not in visited_sector:
                            board[i][j] += lens[lx][ly][0]
                            board[i][j] %= 10
                            visited_sector.add(lens[lx][ly][1])
            print(board[i][j], end="")
        print()


if __name__ == "__main__":
    main()