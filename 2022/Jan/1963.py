import collections
import sys
input = sys.stdin.readline
prime = [True] * 10000
prime[0] = False
prime[1] = False
for i in range(2, 101):
    if prime[i]:
        for j in range(i + i, 10000, i):
            prime[j] = False


def bfs(start, goal):
    queue = collections.deque()
    queue.append((start, 0))
    visited = set()
    visited.add(start)
    while queue:
        num, cnt = queue.popleft()
        if num == goal:
            print(cnt)
            return
        for i in range(4):
            for j in range(-9, 10):
                dx = int(str(num)[3 - i]) + j
                if j != 0 and 0 <= dx <= 9:
                    d_num = j * (10 ** i)
                    l_num = num + d_num
                    if 1000 <= l_num <= 9999 and prime[l_num] and l_num not in visited:
                        visited.add(l_num)
                        queue.append((l_num, cnt + 1))
    print("Impossible")


t = int(input())
for _ in range(t):
    s, g = map(int, input().split())
    bfs(s, g)
