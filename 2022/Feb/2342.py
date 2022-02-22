import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
nums = list(map(int, input().split()))
dp = [[[-1] * 5 for _ in range(5)] for _ in range(len(nums) - 1)]


def move(a, b):
    if a == b:
        return 1
    elif a == 0:
        return 2
    elif abs(b - a) == 2:
        return 4
    else:
        return 3


def recur(n, l, r):
    if n >= len(nums) - 1:
        return 0
    if dp[n][l][r] != -1:
        return dp[n][l][r]

    dp[n][l][r] = min(recur(n + 1, l, nums[n]) + move(r, nums[n]), recur(n + 1, nums[n], r) + move(l, nums[n]))
    return dp[n][l][r]


print(recur(0, 0, 0))