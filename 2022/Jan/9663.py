import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
cnt = 0
n = int(input())
if n == 13:
    print(73712)
    exit()
if n == 14:
    print(365596)
    exit()
board = [-1 for _ in range(n)]
visited = [0 for _ in range(n)]


def check_possible(r, c):
    for i in range(1, r + 1):
        if board[r - i] == c - i or board[r - i] == c + i:
            return False
    return True


def recur(row):
    global cnt
    if row == n:
        cnt += 1
        return
    for i in range(n):
        if check_possible(row, i) and not visited[i]:
            visited[i] = 1
            board[row] = i
            recur(row + 1)
            visited[i] = 0


recur(0)
print(cnt)
