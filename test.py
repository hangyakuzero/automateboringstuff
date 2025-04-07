matrix = [[1, 0], [0, 1], [0, 1]]
matrix2 = [[0, 1, 1, 1], [0, 1, 1], [0, 1, 1]]
matrix3 = [[1, 0], [0, 1], [0, 1]]
print(matrix)
for i in matrix2:
    for j in i:
        print(j, end=" ")
    print("\n")
print("\n")


for i in range(3):
    for j in range(3):
        print(matrix2[i][j], end=" ")
    print("\n")

print(len(matrix2[0]))


def check(m):
    for i in m:
        if len(i) != len(m[0]):
            return False
    return True


check(matrix)
print(check(matrix))
print(check(matrix2))
check(matrix2)
