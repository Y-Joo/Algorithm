import sys
input = sys.stdin.readline


def recur(result, index, consonant_index):
    global l
    vowel_flag = True
    consonant_flag = True
    consonant_cnt = 0
    if len(result) == l:
        sorted_list = sorted(result)
        if sorted_list not in ans:
            ans.append(sorted_list)
        return
    if index >= len(letters):
        return
    for let in result:
        if let in vowels:
            vowel_flag = False
        else:
            consonant_cnt += 1
    if consonant_cnt >= 2:
        consonant_flag = False
    if vowel_flag:
        for vowel in vowels:
            result.append(vowel)
            recur(result, index, consonant_index)
            result.remove(vowel)
    elif consonant_flag:
        for i in range(consonant_index, len(letters)):
            if letters[i] not in vowels and letters[i] not in result:
                result.append(letters[i])
                recur(result, index, i + 1)
                result.remove(letters[i])
    else:
        for i in range(index, len(letters)):
            if letters[i] not in result:
                result.append(letters[i])
                recur(result, i + 1, consonant_index)
                result.remove(letters[i])


l, c = map(int, input().split())
vowels = []
letters = input().rstrip().split()
for ch in letters:
    if ch in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(ch)
ans = []
recur([], 0, 0)
ans.sort()
for word in ans:
    print("".join(word))
