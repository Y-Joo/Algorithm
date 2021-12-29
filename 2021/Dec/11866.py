n, k = map(int, input().split())
index = 0
nums = [i for i in range(1, n + 1)]
killed = []
while nums:
    index += k - 1
    if index >= n:
        index = index % n
    killed.append(nums.pop(index))
    n -= 1

print("<", end="")
for i in range(len(killed)):
    if i:
        print(", ", end="")
    print(killed[i], end="")
print(">")