n, m = map(int, input().split())
known = list(map(int, input().split()))
known = set(known[1:])
cnt = 0
nums = []
for _ in range(m):
    nums.append(list(map(int, input().split())))
for _ in range(m):
    for i in range(m):
        for num in nums[i][1:]:
            if num in known:
                known = known.union(set(nums[i][1:]))

for i in range(m):
    flag = 0
    for num in nums[i][1:]:
        if num in known:
            flag = 1
            break
    if not flag:
        cnt += 1

print(cnt)
