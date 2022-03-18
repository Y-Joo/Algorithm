import heapq
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
nums = [[a[i], b[i]] for i in range(n)]
nums.sort(key=lambda x: x[1])
ans = nums[0][0]
queue = []
for i in range(1, n - 1, 2):
    heapq.heappush(queue, -nums[i][0])
    heapq.heappush(queue, -nums[i + 1][0])
    ans -= heapq.heappop(queue)
print(ans)