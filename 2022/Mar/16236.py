from collections import deque
import sys

input = sys.stdin.readline
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
n = int(input().strip())
data = [list(map(int, input().split())) for _ in range(n)]
q = deque()
fish = []
for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            if data[i][j] == 9:
                q.append((0, 2, i, j))
                data[i][j] = 0
            else:
                fish.append((data[i][j], i, j))
eat = 0
result = 0
while q:
    cost, size, aa, bb = q.popleft()
    test = []
    for i in range(len(fish)):
        if size > fish[i][0]:
            test.append((fish[i][1], fish[i][2]))
    if len(test) == 0:
        result = cost
        break
    comparison = []
    for x, y in test:
        s = deque()
        temp = [[False] * n for _ in range(n)]
        temp[aa][bb] = True
        s.append((0, aa, bb))
        while s:
            ccost, a, b = s.popleft()
            if a == x and b == y:
                comparison.append((ccost, x, y))
                break
            for i in range(4):
                na = a + dx[i]
                nb = b + dy[i]
                if 0 <= na < n and 0 <= nb < n and not temp[na][nb] and data[na][nb] <= size:
                    temp[na][nb] = True
                    s.append((ccost + 1, na, nb))
    comparison.sort()
    if len(comparison) == 0:
        result = cost
        break
    else:
        k = comparison.pop(0)
    eat += 1
    if size == eat:
        size += 1
        eat = 0
    q.append((cost + k[0], size, k[1], k[2]))
    for i in range(len(fish)):
        if fish[i][1] == k[1] and fish[i][2] == k[2]:
            fish.pop(i)
            break
print(result)
