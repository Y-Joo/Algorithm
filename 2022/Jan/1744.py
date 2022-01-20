import sys
input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort(reverse=True)
ans = 0
i = 0
flag = False
stop_point = -2
while i < n:
    if i == stop_point:
        ans += nums[i]
        break
    elif i - 1 == stop_point:
        ans += nums[i] * nums[i - 1]
        break
    elif i == len(nums) - 1 and not flag:
        ans += nums[i]
    elif nums[i] <= 0:
        if not flag:
            stop_point = i
            flag = True
            i = len(nums)
        else:
            ans += nums[i] * nums[i - 1]
            i -= 1
    elif nums[i] == 1:
        ans += nums[i]
    else:
        if nums[i + 1] > 1:
            ans += nums[i] * nums[i + 1]
            i += 1
        else:
            ans += nums[i]
    if flag:
        i -= 1
    else:
        i += 1
print(ans)
