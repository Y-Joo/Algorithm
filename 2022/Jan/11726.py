n = int(input())
dp = [0 for _ in range(n + 3)]
dp[0] = 1
for i in range(n + 1):
    dp[i + 1] += dp[i]
    dp[i + 2] += dp[i]
print(dp[n] % 10007)
