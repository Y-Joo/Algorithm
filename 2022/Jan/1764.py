import sys
input = sys.stdin.readline
n, m = map(int, input().split())
n_listen = set()
result = []
for _ in range(n):
    name = input().rstrip()
    n_listen.add(name)
for _ in range(m):
    name = input().rstrip()
    if name in n_listen:
        result.append(name)
result.sort()
print(len(result))
for name in result:
    print(name)
