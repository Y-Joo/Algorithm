import sys
input = sys.stdin.readline
s1 = list(input().rstrip())
s2 = list(input().rstrip())
dp = [[(0, []) for _ in range(len(s2))] for _ in range(len(s1))]
for i in range(len(s1)):
    for j in range(len(s2)):
        if i == 0:
            if s1[i] == s2[j]:
                dp[i][j] = (1, [s1[i]])
            elif j > 0:
                dp[i][j] = dp[i][j - 1]
        elif j == 0:
            if s1[i] == s2[j]:
                dp[i][j] = (1, [s1[i]])
            else:
                dp[i][j] = dp[i - 1][j]
        else:
            if s1[i] == s2[j]:
                dp[i][j] = (dp[i - 1][j - 1][0] + 1, dp[i - 1][j - 1][1] + [s1[i]])
            else:
                if dp[i - 1][j][0] >= dp[i][j - 1][0]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
if len(s1) <= 0 or len(s2) <= 0:
    print(0)
else:
    print(dp[len(s1) - 1][len(s2) - 1][0])
    if dp[len(s1) - 1][len(s2) - 1][0] > 0:
        print("".join(dp[len(s1) - 1][len(s2) - 1][1]))
