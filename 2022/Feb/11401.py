p = 1000000007
n, k = map(int, input().split())
fact = [1] * (n + 1)
for i in range(2, n + 1):
    fact[i] = fact[i - 1] * i % p


def power(a, b):
    global p
    if b == 0:
        return 1
    elif b % 2:
        return power(a, b // 2) ** 2 * a % p
    else:
        return power(a, b // 2) ** 2 % p


print(power(fact[k] * fact[n - k], p - 2) * fact[n] % p)