class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __add__(self, other):
        matr = []
        for i in range(len(self.lists)):
            matr.append([])
            for j in range(len(self.lists[i])):
               matr[i].append(self.lists[i][j] + other.lists[i][j])

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.lists]))


a = [[3, 5, 35], [2, 4, 6], [-1, 68, 8]]
b = [[31, 22, 15], [37, 43, 6], [51, 86, 34]]

matrix1 = Matrix(a)
matrix2 = Matrix(b)

print(matrix1)
print(matrix2)
s = matrix2 + matrix1
print(s)


