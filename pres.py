def prod(k):
    res = [1 for _ in k]
    prefix = 1
    suffix = 1
    for i in range(1, len(k)):
        prefix *= k[i - 1]
        res[i] = prefix
    for i in range(len(k) - 2, -1, -1):
        suffix *= k[i + 1]
        res[i] *= suffix
    return res


k = [2, 4, 1, 8]
l = [4, 1, 2, 3]
s = [2, 3, 1, 4]
print(prod(k))
print(prod(l))
print(prod(s))
