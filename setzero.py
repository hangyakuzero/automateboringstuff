def setrows(row, m):
    m1 = m
    for j in range(len(m[0])):
        m1[row][j] = 0
    return m1


def setcolumns(column, m):
    m3 = m
    for i in range(len(m)):
        m3[i][column] = 0
    return m3


def setzero(m):
    m1 = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                m1[i] = j
    for i, j in m1.items():
        setrows(i, m)
        setcolumns(j, m)
    return m


def matprint(m):
    for i in m:
        for j in i:
            print(j, end="")
        print("")
    print("\n")


k = [[1, 0], [2, 3]]
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix2 = [[0, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix3 = [[2, 3], [4, 3], [5, 6]]
ls = setzero(matrix1)
ks = setzero(matrix2)
matprint(ls)
matprint(ks)
