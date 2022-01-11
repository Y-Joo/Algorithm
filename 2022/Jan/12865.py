n, k = map(int, input().split())
items = [(0, 0)]
knapsack = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    items.append(list(map(int, input().split())))
for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = items[i][0]
        v = items[i][1]
        if j < w:
            knapsack[i][j] = knapsack[i - 1][j]
        else:
            knapsack[i][j] = max(v + knapsack[i - 1][j - w], knapsack[i - 1][j])
print(knapsack[n][k])
