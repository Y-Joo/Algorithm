import sys
import heapq
input = sys.stdin.readline
t = int (input())
for _ in range(t):
    min_queue = []
    max_queue = []
    n = int(input())
    visited = [True for a in range(n)]
    for i in range(n):
        cmd, n = input().rstrip().split()
        n = int(n)
        if cmd == 'I':
            heapq.heappush(min_queue, (n, i))
            heapq.heappush(max_queue, (-n, i))
        elif cmd == 'D':
            if n == -1:
                while min_queue and not visited[min_queue[0][1]]:
                    heapq.heappop(min_queue)
                if min_queue:
                    visited[heapq.heappop(min_queue)[1]] = False
            elif n == 1:
                while max_queue and not  visited[max_queue[0][1]]:
                    heapq.heappop(max_queue)
                if max_queue:
                    visited[heapq.heappop(max_queue)[1]] = False
    while min_queue and not visited[min_queue[0][1]]:
        heapq.heappop(min_queue)
    while max_queue and not visited[max_queue[0][1]]:
        heapq.heappop(max_queue)
    if not min_queue:
        print("EMPTY")
    else:
        print(max_queue[0][0] * -1, min_queue[0][0])

