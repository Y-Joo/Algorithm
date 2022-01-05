visited = set()
def dfs(graph, n):
    stack = [n]
    visited.add(n)
    while stack:
        x = stack.pop()
        if x in graph.keys():
            for node in graph[x]:
                if node not in visited:
                    stack.append(node)
                    visited.add(node)


import sys
import collections
input = sys.stdin.readline
graph = collections.defaultdict(list)
n, m = map(int, input().split())
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt = 0
for i in range(1, n + 1):
    if i not in visited:
        dfs(graph, i)
        cnt += 1
print(cnt)
