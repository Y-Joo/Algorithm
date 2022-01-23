import math
n = int(input())
prime = [True] * (n + 1)
prime[0] = False
prime[1] = False
prime_list = []
for i in range(2, int(math.sqrt(n)) + 1):
    if prime[i]:
        for j in range(i + i, n + 1, i):
            prime[j] = False
for i in range(2, n + 1):
    if prime[i]:
        prime_list.append(i)
start = 0
cnt = 0
while True:
    if start >= len(prime_list):
        break
    tmp_sum = 0
    for i in range(start, len(prime_list)):
        if tmp_sum + prime_list[i] == n:
            cnt += 1
            break
        elif tmp_sum + prime_list[i] > n:
            break
        else:
            tmp_sum += prime_list[i]
    start += 1
print(cnt)
