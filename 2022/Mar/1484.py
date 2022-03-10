g = int(input())
left = 1
right = 2
ans = []
while True:
    gap = right ** 2 - left ** 2
    if left == right - 1 and gap > g:
        break
    if gap == g:
        ans.append(right)
    if gap >= g:
        left += 1
    else:
        right += 1

if not ans:
    print(-1)
else:
    for num in ans:
        print(num)