n, m = map(int, input().split())
nums = []
dp = [[0 for a in range(m)] for b in range(n)]
for _ in range(n):
    nums.append(input())
max_len = 0
for i in range(n):
    for j in range(m):
        if nums[i][j] == '0':
            dp[i][j] = 0
        else:
            if i == 0 or j == 0:
                dp[i][j] = 1
                max_len = max(max_len, dp[i][j])
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                max_len = max(max_len, dp[i][j])
print(max_len ** 2)
