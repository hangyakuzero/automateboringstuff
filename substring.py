def solution(s):
    l = []
    lon = []
    for i in s:
        if i in l:
            lon.append(len(l))
            l.clear()
            l.append(i)
        else:
            l.append(i)

    return max(lon)


print(solution("abcabcbb"))
print(solution("bbbbbbbbbbb"))
print(solution("abcbbbasdfgghdf"))
