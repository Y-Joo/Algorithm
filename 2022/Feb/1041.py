import sys

n = int(sys.stdin.readline().rstrip("\n"))
nums = list(map(int, sys.stdin.readline().rstrip("\n").split()))
sum = 0
sumLists = []
if (n == 1):
    nums = sorted(nums)
    for i in range(0, 5):
        sum += nums[i]
else:
    sumLists.append(min(nums[0], nums[5]))
    sumLists.append(min(nums[1], nums[4]))
    sumLists.append(min(nums[2], nums[3]))
    sumLists = sorted(sumLists)

    min1 = sumLists[0]
    min2 = sumLists[0] + sumLists[1]
    min3 = sumLists[0] + sumLists[1] + sumLists[2]

    n1 = (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2)
    n2 = 4 * (n - 2) + 4 * (n - 1)
    n3 = 4

    sum += n1 * min1
    sum += n2 * min2
    sum += n3 * min3

print(sum)
