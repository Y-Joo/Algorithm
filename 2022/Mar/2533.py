import collections
import sys

sys.setrecursionlimit(100000000)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dp = [[0, 1] for _ in range(n + 1)]
visited = [0] * (n + 1)


def recur(num):
    visited[num] = 1
    for node in graph[num]:
        if not visited[node]:
            recur(node)
            dp[num][1] += min(dp[node][0], dp[node][1])
            dp[num][0] += dp[node][1]


recur(1)
print(min(dp[1][0], dp[1][1]))
