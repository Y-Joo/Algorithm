import sys
input = sys.stdin.readline
n = int(input())
costs = []
ret = 1000 * 1000 + 1
for _ in range(n):
    costs.append(list(map(int, input().split())))
for init in range(3):
    dp = [[1000 * 1000 + 1] * 3 for _ in range(n)]
    dp[0][init] = costs[0][init]
    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1] + costs[i][0], dp[i - 1][2] + costs[i][0])
        dp[i][1] = min(dp[i - 1][0] + costs[i][1], dp[i - 1][2] + costs[i][1])
        dp[i][2] = min(dp[i - 1][0] + costs[i][2], dp[i - 1][1] + costs[i][2])
    for i in range(3):
        if i == init:
            continue
        ret = min(ret, dp[n - 1][i])
print(ret)
