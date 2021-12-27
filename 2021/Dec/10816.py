import collections
n = int(input())
nums = list(map(int, input().split()))
cnt = collections.Counter(nums)
m = int(input())
cards = list(map(int, input().split()))
for card in cards:
    if card in cnt.keys():
        print(cnt[card], end=' ')
    else:
        print("0", end=' ')