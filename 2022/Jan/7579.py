n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))
sum_cost = sum(cost)
nums = [[0 for a in range(sum_cost + 1)] for b in range(n + 1)]
result = 10001
for i in range(1, n + 1):
    for j in range(1, sum_cost + 1):
        mem = memory[i - 1]
        co = cost[i - 1]
        if co > j:
            nums[i][j] = nums[i - 1][j]
        else:
            nums[i][j] = max(nums[i - 1][j], mem + nums[i - 1][j - co])
        if nums[i][j] >= m:
            result = min(result, j)
print(result)
