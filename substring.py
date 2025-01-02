def solution(s):
    start = 0
    charmap = {}
    maxlen = 0
    for i in range(len(s)):
        if s[i] in charmap and charmap[s[i]] >= start:
            start = charmap[s[i]] + 1
        charmap[s[i]] = i
        maxlen = max(maxlen, i - start + 1)
    return maxlen


print(solution("abcabcbb"))
print(solution("bbbbbbbbbbb"))
print(solution("abcbbbasdfgghdf"))
print(solution("aab"))
print(solution("dvdf"))
