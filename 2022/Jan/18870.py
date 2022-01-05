import sys
import collections
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
sorted_nums = list(set(nums))
sorted_nums.sort()
dic = collections.defaultdict()
for i, x in enumerate(sorted_nums):
    dic[x] = i
for x in nums:
    print(dic[x], end=" ")
