import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    nums = []
    for i in range(n):
        x, y = map(int, input().split())
        nums.append((x, y))
    nums.sort()
    pre = nums[0][1]
    cnt = 1
    for i in range(1, n):
        if nums[i][1] < pre:
            cnt += 1
            pre = nums[i][1]
    print(cnt)
