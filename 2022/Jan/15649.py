def recur(cnt, nums):
    global n, m
    if cnt == m:
        print(*nums)
        return
    for i in range(1, n + 1):
        if i not in nums:
            nums[cnt] = i
            recur(cnt + 1, nums)
            nums[cnt] = 0


n, m = map(int, input().split())
nums = [0] * m
for i in range(1, n + 1):
    nums[0] = i
    recur(1, nums)
