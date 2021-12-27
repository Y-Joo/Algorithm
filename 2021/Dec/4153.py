def check_possible(a, b, c):
    if a * a + b * b == c * c:
        return True
    else:
        return False
while 1:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if check_possible(a, b, c) or check_possible(a, c, b) or check_possible(b, c, a):
        print("right")
    else:
        print("wrong")