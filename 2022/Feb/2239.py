def cal(x, y):
    return (x//3)*3 + (y//3)

def sol(n):
    if n == 81:
        for i in B:
            print(''.join(map(str, i)))
        return True
    x = n // 9
    y = n % 9
    if B[x][y]: return sol(n+1)
    else:
        for i in range(1, 10):
            if not c1[x][i] and not c2[y][i] and not c3[cal(x,y)][i]:
                c1[x][i] = c2[y][i] = c3[cal(x,y)][i] = True
                B[x][y] = i
                if sol(n+1): return True
                c1[x][i] = c2[y][i] = c3[cal(x,y)][i] = False
                B[x][y] = 0
    return False

B = [list(map(int, input())) for _ in range(9)]
c1 = [[False]*10 for _ in range(9)] #행
c2 = [[False]*10 for _ in range(9)] #열
c3 = [[False]*10 for _ in range(9)] #사각형
for i in range(9):
    for j in range(9):
        if B[i][j]:
            c1[i][B[i][j]] = True
            c2[j][B[i][j]] = True
            c3[cal(i, j)][B[i][j]] = True
sol(0)