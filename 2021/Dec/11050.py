import sys


def BC(n, k):
    if n == k or k == 0:
        return 1
    else:
        return BC(n - 1, k - 1) + BC(n - 1, k)
sys.setrecursionlimit(100000)
n, k = map(int, input().split())
print(BC(n, k))