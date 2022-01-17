import collections
dist = [-1 for _ in range(100001)]


def bfs(n, k):
    queue = collections.deque()
    queue.append(n)
    dist[n] = 0
    cnt = 0
    while queue:
        x = queue.popleft()
        if x == k:
            return
        else:
            for nx in (x - 1, x + 1):
                if 0 <= nx <= 100000 and dist[nx] == -1:
                    queue.append(nx)
                    dist[nx] = dist[x] + 1
            if 0 <= x * 2 <= 100000 and (dist[2 * x] == -1 or dist[2 * x] > dist[x]):
                queue.appendleft(2 * x)
                dist[2 * x] = dist[x]


n, k = map(int, input().split())
bfs(n, k)
print(dist[k])
