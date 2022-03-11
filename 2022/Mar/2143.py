import collections
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
sum_a = []
dic_b = collections.defaultdict()
ans = 0
for i in range(n):
    for j in range(i, n):
        sum_a.append(sum(a[i:j + 1]))
for i in range(m):
    for j in range(i, m):
        tmp_sum = sum(b[i:j + 1])
        if tmp_sum in dic_b.keys():
            dic_b[tmp_sum] += 1
        else:
            dic_b[tmp_sum] = 1
for num in sum_a:
    if t - num in dic_b.keys():
        ans += dic_b[t - num]
print(ans)
