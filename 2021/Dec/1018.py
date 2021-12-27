n, m = map(int, input().split())
num = []
for i in range(n):
    s = input()
    num.append(s)
mini = 64
for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2 == 0:
                    if num[x][y] != 'B':
                        cnt1 += 1
                    else:
                        cnt2 += 1
                else:
                    if num[x][y] != 'W':
                        cnt1 += 1
                    else:
                        cnt2 += 1
        mini = min(mini, cnt1, cnt2)
print(mini)