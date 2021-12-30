dp = []
dp.append(0)
dp.append(1)
t = int(input())
for _ in range(t):
    n = int(input())
    cnt_zero = [0 for _ in range(n + 1)]
    cnt_one = [0 for _ in range(n + 1)]

    for i in range(n + 1):
        if i == 0:
            cnt_zero[i] = 1
        elif i == 1:
            cnt_one[i] = 1
        else:
            dp.insert(i, dp[i - 2] + dp[i - 1])
            cnt_zero[i] = cnt_zero[i - 2] + cnt_zero[i - 1]
            cnt_one[i] = cnt_one[i - 2] + cnt_one[i - 1]
    print(cnt_zero[n], end=" ")
    print(cnt_one[n])