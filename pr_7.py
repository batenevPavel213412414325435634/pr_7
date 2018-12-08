from random import random

p = int(input("Введите какой будет максимальный элемент в матрице:"))
N = int(input("Введите размерность матрицы:"))

matrix = []

for i in range(N):
    string = []
    for j in range(N):
        string.append(int(random() * p))
    matrix.append(string)

for string in matrix:
    print(string)

max_str = 0
num_str = 0
i = 0
for string in matrix:
    if sum(string) > max_str:
        max_str = sum(string)
        num_str = i + 1
    i += 1

print("Строка:", num_str, "сумма:", max_str)

max_col = 0
num_col = 0
for i in range(N):
    sum_col = 0
    for j in range(N):
        sum_col += matrix[j][i]
    if sum_col > max_col:
        max_col = sum_col
        num_col = i + 1
print("столбец:", num_col, "сумма:", max_col)

sum_dion = 0
sum_side_dion = 0
for i in range(N):
    sum_dion += matrix[i][i]
    sum_side_dion += matrix[i][N-i-1]

print("Сумма элементов главной диагонали:", sum_dion)
print("Сумма элементов побочной диагонали:", sum_side_dion)
