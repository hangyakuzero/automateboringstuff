def addcols(m, ind):
    for i in m:
        i.insert(ind, 2)


def pp(m):
    for i in m:
        for j in i:
            print(j, end=" ")
        print()
    print()


def som(m):
    k = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 1:
                k.append(j + 1)
    k.reverse()
    for i in k:
        addcols(m, i)


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1 = [[1, 2, 3], [4, 5, 6], [2, 1, 3]]
m2 = [[1, 2, 3], [3, 2, 1], [3, 5, 6]]
som(m)
pp(m)
som(m1)
pp(m1)
som(m2)
pp(m1)
