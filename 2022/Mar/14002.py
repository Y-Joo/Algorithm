import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [[]] * n
for k in range(n):
    dp[k] = [nums[k]]
    for i in range(k):
        if nums[i] < nums[k] and len(dp[i]) >= len(dp[k]):
            dp[k] = dp[i] + [nums[k]]
dp.sort(key=lambda x: len(x), reverse=True)
print(len(dp[0]))
print(*dp[0])