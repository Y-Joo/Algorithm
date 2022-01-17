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
            cnt += 1
        else:
            for nx in (x - 1, x + 1, 2 * x):
                if 0 <= nx <= 100000 and (dist[nx] == -1 or dist[nx] == dist[x] + 1):
                    queue.append(nx)
                    dist[nx] = dist[x] + 1
    return cnt


n, k = map(int, input().split())
cnt = bfs(n, k)
print(dist[k])
print(cnt)
