n = int(input())
bells = list(map(int, input().split()))
k = int(input())
marvels = list(map(int, input().split()))
l = 40000 + 1
dp = [False for _ in range(l)]
dp[0] = True
for i in bells[::-1]:
    visited = [False for _ in range(l)]
    for j in range(l):
        if dp[j] and not visited[j]:
            tmp = j
            while tmp < l and dp[tmp] and not visited[tmp]:
                tmp += i
            if tmp < l:
                dp[tmp] = True
                visited[tmp] = True
            tmp = j
            while tmp > 0 and dp[tmp] and not visited[tmp]:
                tmp -= i
            if tmp > 0:
                dp[tmp] = True
                visited[tmp] = True
for marvel in marvels:
    if dp[marvel]:
        print("Y", end=" ")
    else:
        print("N", end=" ")
