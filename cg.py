import numpy as np

matrix = np.zeros((7, 7), dtype=int)

for i in range(7):
    for j in range(7):
        if i == j:  # Головна діагональ
            matrix[i, j] = i + 1
        elif i + j == 6:  # Діагональ зліва від головної
            matrix[i, j] = (i + 1) + (j + 1)
        else:
            matrix[i, j] = 0

transposed_matrix = matrix.T

print("Вихідна матриця:")
print(matrix)
print("\nТранспонована матриця:")
print(transposed_matrix)
