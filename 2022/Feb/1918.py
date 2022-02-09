import sys
s = sys.stdin.readline().rstrip()
sign = {'+', '-', '*', '/', '(', ')'}
i = 0
stack = []
for c in s:
    if c in sign:
        if c == '(':
            stack.append(c)
        elif c == '*' or c == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                print(stack.pop(), end="")
            stack.append(c)
        elif c == '+' or c == '-':
            while stack and stack[-1] != '(':
                print(stack.pop(), end="")
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                print(stack.pop(), end="")
            stack.pop()
    else:
        print(c, end="")
while stack:
    print(stack.pop(), end="")
