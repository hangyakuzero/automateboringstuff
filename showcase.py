def check(matrix):
    for i in matrix:
        if (len(i)) != len(matrix[0]):
            return False
    return True


def matshow(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print()


def disp(matrix):
    if check(matrix):
        matshow(matrix)
    else:
        print("not a valid matrix")


def takematrix():
    x = []
    rows = int(input("enter the number of rows"))
    col = int(input("enter the number of columns"))
    for i in range(rows):
        i = []
        for j in range(col):
            k = int(input("enter the number"))
            i.append(k)
        x.append(i)
    return x


def betway():
    x = []
    rows = int(input("enter the number of rows"))
    for i in range(rows):
        k = input("enter the value in rows, space separated:").split()
        for element in k:
            element = int(element)
        x.append(k)
    return x


matrix1 = [[1, 0], [0, 1]]
matrix2 = [[1, 0, 0], [0, 1]]
matrix3 = [[0, 1], [1, 0], [0, 1]]
print(len(matrix3))
print(len(matrix3[0]))
matrix4 = [[1, 0], [1, 2, 3], [0, 1]]
