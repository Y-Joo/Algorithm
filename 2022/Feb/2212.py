import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
nums = list(map(int, input().split()))
nums.sort()
gap = []
for i in range(1, len(nums)):
    gap.append(nums[i] - nums[i - 1])
gap.sort()
for i in range(k - 1):
    if gap:
        gap.pop()
print(sum(gap))
