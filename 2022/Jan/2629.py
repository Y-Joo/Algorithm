import collections
n = int(input())
bells = list(map(int, input().split()))
k = int(input())
marvels = list(map(int, input().split()))
l = 40000 + 1
dp = collections.defaultdict()
dp[0] = True
for i in bells[::-1]:
    append_list = []
    for j in dp.keys():
        if (j + i) not in dp.keys():
            append_list.append(j + i)
        if (j - i) not in dp.keys():
            append_list.append(j - i)
    for a in append_list:
        dp[a] = True
result = []
for marvel in marvels:
    if marvel in dp.keys() and dp[marvel]:
        result.append("Y")
    else:
        result.append("N")
print(*result)
