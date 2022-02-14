import collections
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
indegree = [0] * (n + 1)
queue = collections.deque()
graph = collections.defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)
for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)
while queue:
    cur = queue.popleft()
    print(cur, end=" ")
    for node in graph[cur]:
        indegree[node] -= 1
        if indegree[node] <= 0:
            queue.append(node)

