n = int(input())
nums = list(map(int, input().split()))
dp = [[0] * 21 for _ in range(n)]
for i in range(n):
    if i == 0:
        dp[i][nums[i]] = 1
    else:
        for j in range(21):
            if dp[i - 1][j]:
                num = dp[i - 1][j]
                if 0 <= j + nums[i] <= 20:
                    dp[i][j + nums[i]] += num
                if 0 <= j - nums[i] <= 20:
                    dp[i][j - nums[i]] += num
print(dp[n - 2][nums[n - 1]])
