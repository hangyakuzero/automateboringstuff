# take a list
l = [i for i in range(2, 101)]


def sieve(li):
    k = len(li)
    i = 0
    while i < k:
        for s in range(2, (k // 2) + 2):
            m = li[i] * s
            if m in li:
                li.remove(m)
        k = len(li)
        i += 1
    return li


print(sieve(l))
