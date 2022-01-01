import collections
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
poc = []
dic = collections.defaultdict()
for i in range(n):
    name = input().rstrip()
    poc.append(name)
    dic[name] = i + 1
for _ in range(m):
    cmd = input().rstrip()
    if '0' <= cmd[0] <= '9':
        print(poc[int(cmd) - 1])
    else:
        print(dic[cmd])
