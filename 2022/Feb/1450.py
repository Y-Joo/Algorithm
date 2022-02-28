n, c = map(int, input().split())
items = list(map(int, input().split()))
aw = items[:n // 2]
bw = items[n // 2:]
asum = []
bsum = []


def brute(tw, tsum, i, w):
    if i >= len(tw):
        tsum.append(w)
        return
    brute(tw, tsum, i + 1, w)
    brute(tw, tsum, i + 1, w + tw[i])


def binary(k):
    start = 0
    end = len(bsum)
    while start < end:
        mid = (start + end) // 2
        if bsum[mid] <= k:
            start = mid + 1
        else:
            end = mid
    return start


brute(aw, asum, 0, 0)
brute(bw, bsum, 0, 0)
bsum.sort()
ans = 0
for i in asum:
    if c - i < 0:
        continue
    else:
        ans += binary(c - i)
print(ans)
