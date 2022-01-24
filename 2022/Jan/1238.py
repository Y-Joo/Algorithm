import sys
import collections
import heapq
input = sys.stdin.readline
INF = sys.maxsize
n, m, x = map(int, input().split())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start, goal):
    q = [(0, start)]
    distance = [INF] * (n + 1)
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for item in graph[node]:
            if dist + item[1] < distance[item[0]]:
                distance[item[0]] = dist + item[1]
                heapq.heappush(q, (distance[item[0]], item[0]))
    return distance[goal]


max_dist = -1
for i in range(1, n + 1):
    if i != x:
        max_dist = max(max_dist, dijkstra(i, x) + dijkstra(x, i))
print(max_dist)
