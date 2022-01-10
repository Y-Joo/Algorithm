import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [[-1 for i in range(n)] for j in range(n)]
def palindrom(a, b):
    global n
    sum = b + a
    if sum % 2:
        x = sum // 2
        y = (sum + 1) // 2
    else:
        x = sum // 2
        y = sum // 2
    while x >= a and y <= b and nums[x] == nums[y]:
        dp[x][y] = 1
        x -= 1
        y += 1
    while x >= a and y <= b:
        dp[x][y] = 0
        x -= 1
        y += 1


m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    if dp[s - 1][e - 1] != -1:
        print(dp[s - 1][e - 1])
    else:
        palindrom(s - 1, e - 1)
        print(dp[s - 1][e - 1])
