n = int(input())
nums = list(map(int, input().split()))
dp = [0]
for num in nums:
    if num > dp[-1]:
        dp.append(num)
    else:
        left = 0
        right = len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        dp[left] = num
print(len(dp) - 1)
