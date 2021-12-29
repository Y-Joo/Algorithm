import sys
input = sys.stdin.readline
queue = []
n = int(input())
for _ in range(n):
    cmd = input().strip()
    c = cmd.split()
    cmd = c[0]
    if cmd == "push":
        queue.append(int(c[1]))
    elif cmd == "pop":
        if not queue:
            print(-1)
        else:
            x = queue.pop(0)
            print(x)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif cmd == "back":
        if not queue:
            print(-1)
        else:
            print(queue[len(queue) - 1])
