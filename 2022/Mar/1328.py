n, l, r = map(int, input().split())
dp = [[[0] * (r + 1) for _ in range(l + 1)] for _ in range(n + 1)]
dp[1][1][1] = 1
for i in range(1, n + 1):
    for j in range(1, l + 1):
        for k in range(1, r + 1):
            dp[i][j][k] += dp[i - 1][j - 1][k]
            dp[i][j][k] += dp[i - 1][j][k - 1]
            dp[i][j][k] += dp[i - 1][j][k] * (i - 2)
            dp[i][j][k] %= 1000000007
print(dp[n][l][r])
