n = int(input())
min_dp = [0] * 3
max_dp = [0] * 3
for i in range(n):
    nums = list(map(int, input().split()))
    if i == 0:
        for j in range(3):
            min_dp[j] = nums[j]
            max_dp[j] = nums[j]
    else:
        min_a = min(min_dp[0], min_dp[1])
        min_b = min(min_dp)
        min_c = min(min_dp[1], min_dp[2])
        max_a = max(max_dp[0], max_dp[1])
        max_b = max(max_dp)
        max_c = max(max_dp[1], max_dp[2])
        min_dp[0] = min_a + nums[0]
        min_dp[1] = min_b + nums[1]
        min_dp[2] = min_c + nums[2]
        max_dp[0] = max_a + nums[0]
        max_dp[1] = max_b + nums[1]
        max_dp[2] = max_c + nums[2]
print(max(max_dp), min(min_dp))

