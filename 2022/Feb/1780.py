n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
mi = 0
zero = 0
one = 0


def cut(x, y, k):
    global mi, zero, one
    check = board[x][y]
    for i in range(x, x + k):
        for j in range(y, y + k):
            if board[i][j] != check:
                cut(x, y, k // 3)
                cut(x + k // 3, y, k // 3)
                cut(x + 2 * k // 3, y, k // 3)
                cut(x, y + k // 3, k // 3)
                cut(x + k // 3, y + k // 3, k // 3)
                cut(x + 2 * k // 3, y + k // 3, k // 3)
                cut(x, y + 2 * k // 3, k // 3)
                cut(x + k // 3, y + 2 * k // 3, k // 3)
                cut(x + 2 * k // 3, y + 2 * k // 3, k // 3)
                return
    if check == -1:
        mi += 1
    elif check == 0:
        zero += 1
    elif check == 1:
        one += 1


cut(0, 0, n)
print(mi)
print(zero)
print(one)