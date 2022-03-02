import bisect
n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)
arr = [-1000000001]
max_val = 0
for i in range(1, n + 1):
    if nums[i] > arr[-1]:
        arr.append(nums[i])
        dp[i] = len(arr) - 1
        max_val = dp[i]
    else:
        dp[i] = bisect.bisect_left(arr, nums[i])
        arr[dp[i]] = nums[i]
print(max_val)
ans = []
for i in range(n, 0, -1):
    if dp[i] == max_val:
        ans.append(nums[i])
        max_val -= 1
ans.reverse()
print(*ans)
