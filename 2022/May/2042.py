import collections
import sys
input = sys.stdin.readline
n, m, k = map(int, input().split())
nums = []
dic = collections.defaultdict()
for _ in range(n):
    nums.append(int(input()))
dp = [0 for _ in range(n)]
dp[0] = nums[0]
for i in range(1, n):
    dp[i] = dp[i - 1] + nums[i]
for _ in range(m + k):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        dic[cmd[1] - 1] = cmd[2]
    elif cmd[0] == 2:
        if cmd[1] - 2 >= 0:
            result = dp[cmd[2] - 1] - dp[cmd[1] - 2]
        else:
            result = dp[cmd[2] - 1]
        for key in dic.keys():
            if cmd[1] - 1 <= key <= cmd[2] - 1:
                result += dic[key] - nums[key]
        print(result)
