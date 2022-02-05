import sys
input = sys.stdin.readline
n, s = map(int, input().split())
nums = list(map(int, input().split()))
min_dis = 1e9
start = 0
end = 0
sum = nums[0]
while end < n and min_dis > 1:
    if sum < s:
        end += 1
        if end >= n:
            break
        sum += nums[end]
    else:
        min_dis = min(min_dis, end - start + 1)
        if end == start:
            break
        sum -= nums[start]
        start += 1

if min_dis == 1e9:
    print(0)
else:
    print(min_dis)
