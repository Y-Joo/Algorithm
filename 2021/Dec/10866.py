import sys
input = sys.stdin.readline
deque = []
n = int(input())
for _ in range(n):
    cmd = input().strip()
    c = cmd.split()
    cmd = c[0]
    if cmd == "push_front":
        deque.insert(0, int(c[1]))
    elif cmd == "push_back":
        deque.append(int(c[1]))
    elif cmd == "pop_front":
        if not deque:
            print(-1)
        else:
            x = deque.pop(0)
            print(x)
    elif cmd == "pop_back":
        if not deque:
            print(-1)
        else:
            x = deque.pop()
            print(x)
    elif cmd == "size":
        print(len(deque))
    elif cmd == "empty":
        if not deque:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if not deque:
            print(-1)
        else:
            print(deque[0])
    elif cmd == "back":
        if not deque:
            print(-1)
        else:
            print(deque[len(deque) - 1])
