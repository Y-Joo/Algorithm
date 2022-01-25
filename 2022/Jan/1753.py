import sys
import collections
import heapq
input = sys.stdin.readline
INF = sys.maxsize
n, m = map(int, input().split())
x = int(input())
graph = collections.defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
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
    return distance


dist = dijkstra(x)
for i in range(1, n + 1):
    if i == x:
        print(0)
    else:
        if dist[i] == INF:
            print("INF")
        else:
            print(dist[i])
