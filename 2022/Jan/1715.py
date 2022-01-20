import heapq
n = int(input())
queue = []
for _ in range(n):
    heapq.heappush(queue, int(input()))
ans = 0
while len(queue) > 1:
    a = heapq.heappop(queue)
    b = heapq.heappop(queue)
    ans += (a + b)
    heapq.heappush(queue, a + b)
print(ans)
