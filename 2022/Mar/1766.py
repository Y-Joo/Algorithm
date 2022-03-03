import collections
import heapq
n, m = map(int, input().split())
dic = collections.defaultdict(list)
indegree = [0] * (n + 1)
queue = []
for _ in range(m):
    a, b = map(int, input().split())
    dic[a].append(b)
    indegree[b] += 1
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)
ans = []
while queue:
    now = heapq.heappop(queue)
    ans.append(now)
    for node in dic[now]:
        indegree[node] -= 1
        if not indegree[node]:
            heapq.heappush(queue, node)
print(*ans)