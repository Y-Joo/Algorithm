import collections
import sys
input = sys.stdin.readline
def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = [0] + list(map(int, input().split()))
        dic = collections.defaultdict(list)
        indegree = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                dic[nums[i]].append(nums[j])
                indegree[nums[j]] += 1
        queue = collections.deque()
        m = int(input())
        for _ in range(m):
            a, b = map(int, input().split())
            if b in dic[a]:
                dic[a].remove(b)
                dic[b].append(a)
                indegree[a] += 1
                indegree[b] -= 1
            else:
                dic[b].remove(a)
                dic[a].append(b)
                indegree[a] -= 1
                indegree[b] += 1
        for i in range(1, n + 1):
            if not indegree[i]:
                queue.append(i)
        ans = []
        flag = False
        while queue:
            now = queue.popleft()
            ans.append(now)
            for node in dic[now]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    queue.append(node)
            if len(queue) > 1:
                flag = True
                break
        if flag:
            print("?")
        elif len(ans) != n:
            print("IMPOSSIBLE")
        else:
            print(*ans)


if __name__ == "__main__":
    main()