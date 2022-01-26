import collections

n = int(input())
nums = []
indegree = []
queue = collections.deque()
for i in range(n):
    nums.append(list(map(int, input().split())))
    indegree.append(len(nums[i][1:-1]))
    if indegree[i] == 0:
        queue.append(i + 1)
dp = [0] * n
while queue:
    num = queue.popleft()
    dp[num - 1] += nums[num - 1][0]
    for i in range(n):
        if num in nums[i][1:-1]:
            indegree[i] -= 1
            dp[i] = max(dp[num - 1], dp[i])
            if indegree[i] == 0:
                queue.append(i + 1)
for i in range(n):
    print(dp[i])
