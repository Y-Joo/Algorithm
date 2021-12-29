import sys
input = sys.stdin.readline
stack = []
n = int(input())
for _ in range(n):
    cmd = input().strip()
    c = cmd.split()
    cmd = c[0]
    if cmd == "push":
        stack.append(int(c[1]))
    elif cmd == "pop":
        if not stack:
            print(-1)
        else:
            x = stack.pop()
            print(x)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif cmd == "top":
        if not stack:
            print(-1)
        else:
            print(stack[len(stack) - 1])