import sys
input = sys.stdin.readline
def main():
    n, m = map(int, input().split())
    profit = [[0] * (m + 1)]
    for _ in range(n):
        profit.append(list(map(int, input().split())))
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    pos = [[[0 for _ in range(m + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i][j - 1], profit[i][j])
            if dp[i][j] == profit[i][j]:
                pos[i][j][j] = i
            else:
                pos[i][j] = pos[i][j - 1].copy()
            for k in range(1, i):
                if dp[i][j] < dp[k][j - 1] + profit[i - k][j]:
                    dp[i][j] = dp[k][j - 1] + profit[i - k][j]
                    pos[i][j] = pos[k][j - 1].copy()
                    pos[i][j][j] = i - k
    print(dp[-1][-1])
    print(*pos[-1][-1][1:])




if __name__=="__main__":
    main()