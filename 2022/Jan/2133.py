n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
for i in range(2, n + 1, 2):
    dp[i] += 3 * dp[i - 2]
    for j in range(0, i - 2, 2):
        dp[i] += 2 * dp[j]
print(dp[n])
