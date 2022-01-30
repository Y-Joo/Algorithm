n = int(input())
nums = list(map(int, input().split()))
nums.sort()
target = 1
for num in nums:
    if target < num:
        break
    target += num
print(target)