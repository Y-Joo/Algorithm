import sys

n = int(input())
nums = list(map(int, input().split()))
p, q = 0, n - 1
val = abs(nums[q] + nums[p])
min_p = nums[p]
min_q = nums[q]
while q > p:
    if nums[p] + nums[q] == 0:
        print(nums[p], nums[q])
        sys.exit()
    else:
        if abs(nums[p] + nums[q]) < val:
            val = abs(nums[p] + nums[q])
            min_p = nums[p]
            min_q = nums[q]
        if nums[p] + nums[q] < 0:
            p += 1
        else:
            q -= 1
print(min_p, min_q)
