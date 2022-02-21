import collections
import sys

n = int(input())
visited = set()


def bfs():
    global n
    queue = collections.deque()
    queue.append((n, [n], 0))
    while queue:
        k, nums, cnt = queue.popleft()
        if k == 1:
            print(cnt)
            print(*nums)
            break
        if k % 3 == 0 and k // 3 not in visited:
            visited.add(k // 3)
            queue.append((k // 3, nums + [k // 3], cnt + 1))
        if k % 2 == 0 and k // 2 not in visited:
            visited.add(k // 2)
            queue.append((k // 2, nums + [k // 2], cnt + 1))
        if k - 1 not in visited:
            visited.add(k - 1)
            queue.append((k - 1, nums + [k - 1], cnt + 1))


bfs()
