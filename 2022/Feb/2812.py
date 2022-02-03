import sys
input = sys.stdin.readline
n, k = map(int, input().split())
num_list = list(map(int, input().strip()))
stack = []
i = 0
for i in range(n):
    while stack and k:
        if num_list[i] > stack[len(stack) - 1]:
            stack.pop()
            k -= 1
        else:
            break
    stack.append(num_list[i])

for i in range(len(stack) - k):
    print(stack[i], end="")

