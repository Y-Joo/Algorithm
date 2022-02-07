import collections
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    delays = [0] + list(map(int, input().split()))
    graph = collections.defaultdict(list)
    indegree = [0] * (n + 1)
    queue = collections.deque()
    dp = [0] * (n + 1)
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(input())
    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = delays[i]
    while queue:
        cur = queue.popleft()
        for node in graph[cur]:
            indegree[node] -= 1
            dp[node] = max(dp[node], dp[cur] + delays[node])
            if indegree[node] == 0:
                queue.append(node)
    print(dp[w])
