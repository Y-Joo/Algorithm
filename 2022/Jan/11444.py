import collections
n = int(input())
dp = collections.defaultdict()
def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x in dp.keys():
        return dp[x]
    else:
        if x % 2:
            m = (x + 1) // 2
            t1 = fibo(m)
            t2 = fibo(m - 1)
            dp[x] = (t1 ** 2 + t2 ** 2) % 1000000007
            return dp[x]
        else:
            m = x // 2
            t1 = fibo(m - 1)
            t2 = fibo(m)
            dp[x] = (2 * t1 + t2) * t2 % 1000000007
            return dp[x]


print(fibo(n))
