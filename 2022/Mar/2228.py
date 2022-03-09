import sys
input = sys.stdin.readline
n, m = map(int, input().split())
con_dp = [[0] + [-1000000000] * m for _ in range(n + 1)]
notcon_dp = [[0] + [-1000000000] * m for _ in range(n + 1)]
for i in range(1, n + 1):
    num = int(input())
    for j in range(1, min(m + 1, int((i + 1) // 2) + 1)):
        con_dp[i][j] = max(con_dp[i - 1][j] + num, notcon_dp[i - 1][j - 1] + num)
        notcon_dp[i][j] = max(con_dp[i - 1][j], notcon_dp[i - 1][j])
print(max(con_dp[n][m], notcon_dp[n][m]))