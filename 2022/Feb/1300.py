n = int(input())
k = int(input())


def binary_search(start, end):
    global n, k
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for i in range(1, n + 1):
            tmp += min(mid // i, n)
        if tmp < k:
            start = mid + 1
        else:
            end = mid - 1
    return start


print(binary_search(1, n * n))
