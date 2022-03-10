import collections
import sys
input = sys.stdin.readline
n = int(input())
A = []
B = []
C = []
D = []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
sum_a = []
sum_b = collections.defaultdict()
for i in range(n):
    for j in range(n):
        sum_a.append(A[i] + B[j])
for i in range(n):
    for j in range(n):
        if C[i] + D[j] in sum_b.keys():
            sum_b[C[i] + D[j]] += 1
        else:
            sum_b[C[i] + D[j]] = 1
cnt = 0
for num in sum_a:
    if -num in sum_b.keys():
        cnt += sum_b[-num]
print(cnt)
