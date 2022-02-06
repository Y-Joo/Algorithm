import heapq
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
jews = []
bags = []
for _ in range(n):
    m, c = map(int, input().split())
    heapq.heappush(jews, (m, c))
for _ in range(k):
    heapq.heappush(bags, int(input()))
sum_cost = 0
capable = []
while bags:
    bag = heapq.heappop(bags)
    while jews:
        jew = heapq.heappop(jews)
        if jew[0] <= bag:
            heapq.heappush(capable, -jew[1])
        else:
            heapq.heappush(jews, jew)
            break
    if capable:
        sum_cost -= heapq.heappop(capable)
print(sum_cost)
