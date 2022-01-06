t = int(input())
for _ in range(t):
    nums = []
    n = int(input())
    for i in range(2):
        nums.append(list(map(int, input().split())))
    for j in range(1, n):
        for i in range(2):
            if j - 2 < 0:
                nums[i][j] += nums[(i + 1) % 2][j - 1]
            else:
                nums[i][j] += max(nums[(i + 1) % 2][j - 2], nums[(i + 1) % 2][j - 1])
    print(max(nums[0][n - 1], nums[1][n - 1]))
