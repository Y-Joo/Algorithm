import sys
input = sys.stdin.readline
nums = []
n = int(input())
for _ in range(n):
    nums.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(3):
        if j == 0:
            nums[i][j] += min(nums[i - 1][1], nums[i - 1][2])
        elif j == 1:
            nums[i][j] += min(nums[i - 1][0], nums[i - 1][2])
        elif j == 2:
            nums[i][j] += min(nums[i - 1][0], nums[i - 1][1])
print(min(nums[n - 1]))