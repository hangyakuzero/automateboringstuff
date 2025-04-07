l = [100, 20, 4, 80, 1, 2, 3]


def lcs(l):
    s = set(l)
    length = 0
    k = 0
    for i in l:
        if (i - 1) not in s:
            length = 0
            while (i + length) in s:
                length += 1
            k = max(k, length)
    return k


print(lcs(l))
