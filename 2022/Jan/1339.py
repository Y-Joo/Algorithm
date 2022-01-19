import collections
n = int(input())
dic = collections.defaultdict()
for _ in range(n):
    word = input()
    len_word = len(word)
    for i in range(len_word):
        if word[i] in dic.keys():
            dic[word[i]] += 10 ** (len_word - i - 1)
        else:
            dic[word[i]] = 10 ** (len_word - i - 1)
val_list = []
for val in dic.values():
    val_list.append(val)
val_list.sort(reverse=True)
mul = 9
ans = 0
for val in val_list:
    ans += mul*val
    mul -= 1
print(ans)