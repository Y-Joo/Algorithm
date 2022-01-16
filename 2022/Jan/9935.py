import sys
input = sys.stdin.readline
s = input().rstrip()
boom = input().rstrip()
stack = []
for c in s:
    stack.append(c)
    if len(stack) >= len(boom) and "".join(stack[-len(boom):]) == boom:
        for _ in range(len(boom)):
            stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")
