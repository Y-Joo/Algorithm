import sys
input = sys.stdin.readline
s1 = [0] + list(input().rstrip())
s2 = [0] + list(input().rstrip())
len_s1 = len(s1)
len_s2 = len(s2)
dp = [[0] * len_s2 for _ in range(len_s1)]
max_len = 0
for i in range(1, len_s1):
    for j in range(1, len_s2):
        if s1[i] == s2[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_len = max(max_len, dp[i][j])
print(max_len)