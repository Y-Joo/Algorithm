import heapq
import sys
input = sys.stdin.readline
n = int(input())
times = []
for _ in range(n):
    a, b = map(int, input().split())
    times.append((a, b))
times.sort()
heap = []
heapq.heappush(heap, times[0][1])
for i in range(1, n):
    if heap[0] > times[i][0]:
        heapq.heappush(heap, times[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, times[i][1])
print(len(heap))