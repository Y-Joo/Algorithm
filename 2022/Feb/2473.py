import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
nums.sort()
left = nums[0]
right = nums[n - 1]
center = nums[1]
val = abs(left + right + center)
for pivot in range(1, n - 1):
    p = pivot - 1
    q = pivot + 1
    while p >= 0 and q < n:
        tmp_sum = nums[pivot] + nums[p] + nums[q]
        if tmp_sum == 0:
            print(nums[p], nums[pivot], nums[q])
            sys.exit()
        else:
            if abs(tmp_sum) < val:
                val = abs(tmp_sum)
                left = nums[p]
                right = nums[q]
                center = nums[pivot]
            if tmp_sum < 0:
                q += 1
            else:
                p -= 1
print(left, center, right)
