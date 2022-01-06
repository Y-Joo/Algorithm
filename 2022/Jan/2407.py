def fac(x):
    dp = [1 for _ in range(x + 1)]
    for i in range(2, x + 1):
        dp[i] = dp[i - 1] * i
    return dp[x]


n, m = map(int, input().split())
print(fac(n) // fac(n - m) // fac(m))