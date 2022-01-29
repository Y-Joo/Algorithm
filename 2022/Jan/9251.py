s1 = input()
s2 = input()
len_s1 = len(s1)
len_s2 = len(s2)
mat = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
for i in range(1, len_s1 + 1):
    for j in range(1, len_s2 + 1):
        if s1[i - 1] == s2[j - 1]:
            mat[i][j] = mat[i - 1][j - 1] + 1
        else:
            mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])
print(mat[- 1][-1])