t = int(input())
for _ in range(t):
    n = int(input())
    dp = [0 for a in range(n + 4)]
    dp[0] = 1
    for i in range(n + 1):
        dp[i + 1] += dp[i]
        dp[i + 2] += dp[i]
        dp[i + 3] += dp[i]
    print(dp[n])
