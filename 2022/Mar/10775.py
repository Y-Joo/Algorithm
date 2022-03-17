import collections
import sys
input = sys.stdin.readline
g = int(input())
p = int(input())
gate = collections.defaultdict()
cnt = 0
for i in range(p):
    n = int(input())
    if n > g:
        n = g
    while 0 < n and n in gate.keys():
        t = gate[n]
        gate[n] += 1
        n -= t
    if n == 0:
        break
    gate[n] = 1
    cnt += 1
print(cnt)
