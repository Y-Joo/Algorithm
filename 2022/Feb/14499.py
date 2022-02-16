import sys
input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
cmds = list(map(int, input().split()))
up = 0
down = 0
east = 0
west = 0
north = 0
south = 0
for cmd in cmds:
    if cmd == 1 and y + 1 < m:
        east, up, west, down = up, west, down, east
        y += 1
    elif cmd == 2 and y - 1 >= 0:
        west, up, east, down = up, east, down, west
        y -= 1
    elif cmd == 3 and x - 1 >= 0:
        north, up, south, down = up, south, down, north
        x -= 1
    elif cmd == 4 and x + 1 < n:
        south, up, north, down = up, north, down, south
        x += 1
    else:
        continue
    if board[x][y] == 0:
        board[x][y] = down
    else:
        down = board[x][y]
        board[x][y] = 0
    print(up)

