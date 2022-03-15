n, k = map(int, input().split())
nums = list(map(int, input().split()))
mult = set()
cnt = 0
start = 0
while start < k and len(mult) < n:
    mult.add(nums[start])
    start += 1
for i in range(start, k):
    if nums[i] in mult:
        continue
    else:
        temp_set = set()
        for j in range(i + 1, k):
            if nums[j] in mult:
                temp_set.add(nums[j])
                if len(temp_set) == n:
                    mult.remove(nums[j])
                    mult.add(nums[i])
                    break
        else:
            temp_list = list(mult)
            for num in temp_list:
                if num not in temp_set:
                    mult.remove(num)
                    mult.add(nums[i])
                    break
        cnt += 1
print(cnt)
