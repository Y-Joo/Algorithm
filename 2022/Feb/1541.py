import sys

s = sys.stdin.readline().rstrip()
nums = s.split('-')
ans = 0
for i in range(len(nums)):
    if i == 0:
        ans += sum(list(map(int, nums[i].split('+'))))
    else:
        ans -= sum(list(map(int, nums[i].split('+'))))
print(ans)