import sys
input = sys.stdin.readline
nums = set()
m = int(input())
for _ in range(m):
    s = input().rstrip()
    if s == "all":
        nums = set([i for i in range(1, 21)])
    elif s == "empty":
        nums.clear()
    else:
        cmd, n = s.split()
        n = int(n)
        if cmd == "add" and n not in nums:
            nums.add(n)
        elif cmd == "remove" and n in nums:
            nums.remove(n)
        elif cmd == "check":
            if n in nums:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if n in nums:
                nums.remove(n)
            else:
                nums.add(n)
