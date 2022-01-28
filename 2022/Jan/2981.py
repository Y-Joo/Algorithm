import sys
import math
input = sys.stdin.readline
n = int(input())
nums = []
gcd = 0
ans = []
for i in range(n):
    nums.append(int(input()))
    if i == 1:
        gcd = abs(nums[1] - nums[0])
    gcd = math.gcd(gcd, abs(nums[i] - nums[i - 1]))
for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        ans.append(i)
        ans.append(gcd // i)
ans.append(gcd)
ans = list(set(ans))
ans.sort()
print(*ans)
