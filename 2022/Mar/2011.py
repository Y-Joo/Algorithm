import sys

nums = list(map(int, list(input())))
dp = [0] * (len(nums))
if len(nums) == 0:
    print(0)
    sys.exit()
if nums[0] == 0:
    print(0)
    sys.exit()
dp[0] = 1
if len(nums) == 1:
    print(dp[0])
    sys.exit()
elif nums[0] > 2 and nums[1] == 0:
    print(0)
    sys.exit()
if (nums[0] == 1 or nums[0] == 2) and nums[1] == 0:
    dp[1] = 1
elif nums[0] == 1 or (nums[0] == 2 and 0 <= nums[1] <= 6):
    dp[1] = 2
else:
    dp[1] = 1
prev_num = nums[1]
for i in range(2, len(nums)):
    if (prev_num == 0 or prev_num > 2) and nums[i] == 0:
        print(0)
        sys.exit()
    elif (prev_num == 1 or prev_num == 2) and nums[i] == 0:
        dp[i] += dp[i - 2]
    elif prev_num == 1 or (prev_num == 2 and 0 <= nums[i] <= 6):
        dp[i] += dp[i - 2]
        dp[i] += dp[i - 1]
    else:
        dp[i] += dp[i - 1]
    prev_num = nums[i]
    dp[i] %= 1000000
print(dp[len(nums) - 1])
