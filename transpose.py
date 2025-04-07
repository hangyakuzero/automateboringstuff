def trans(m):
    m1 = []
    rows = len(m)
    columns = len(m[0])
    for i in range(columns):
        p = []
        for j in range(rows):
            k = m[j][i]
            p.append(k)
        m1.append(p)
    return m1


def mat(m):
    for i in m:
        for j in i:
            print(j, end=" ")
        print()


def showtrans(m):
    mat(m)
    print("The Transpose is \n")
    mat(trans(m))
    print("\n")
