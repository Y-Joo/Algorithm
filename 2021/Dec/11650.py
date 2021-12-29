n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))
points.sort()
for point in points:
    print(point[0], point[1])