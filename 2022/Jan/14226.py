import collections
s = int(input())
times = [[-1] * (s + 1) for _ in range(s + 1)]
queue = collections.deque()
queue.append((1, 0))
times[1][0] = 0
while queue:
    scr, clip = queue.popleft()
    if scr == s:
        print(times[scr][clip])
        break
    deg = [-1, clip, 0]
    for i in range(3):
        d_scr = scr + deg[i]
        if d_scr > s or d_scr < 1:
            continue
        if i == 2 and times[d_scr][d_scr] == -1:
            queue.append((d_scr, d_scr))
            times[d_scr][d_scr] = times[d_scr][clip] + 1
        elif times[d_scr][clip] == -1:
            queue.append((d_scr, clip))
            times[d_scr][clip] = times[scr][clip] + 1


