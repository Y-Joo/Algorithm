import heapq
import sys
input = sys.stdin.readline
left_heap = []
right_heap = []

def insert_heap(num):
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    if right_heap:
        if -left_heap[0] > right_heap[0]:
            tmp_left = heapq.heappop(left_heap)
            tmp_right = heapq.heappop(right_heap)
            heapq.heappush(right_heap, -tmp_left)
            heapq.heappush(left_heap, -tmp_right)


n = int(input())
for _ in range(n):
    x = int(input())
    insert_heap(x)
    print(-left_heap[0])
