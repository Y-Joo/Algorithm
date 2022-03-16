import sys

input = sys.stdin.readline
while True:
    nums = list(map(int, input().split())) + [0]
    n = nums[0]
    if n == 0:
        break
    stack = []
    ans = 0
    for i in range(1, n + 2):
        w = i
        while stack and nums[i] < stack[-1][1]:
            tmp = stack.pop()
            w = tmp[0]
            ans = max(ans, (i - w) * tmp[1])
        stack.append((w, nums[i]))
    print(ans)
