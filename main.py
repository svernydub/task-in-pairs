import numpy as np
import pandas as pd

matrix = np.array([[1, 2, 3], [4, 5, 6]])

matrix_1d = matrix.reshape(-1)


mean_1d = np.mean(matrix_1d)


std_1d = np.std(matrix_1d)


matrix_2d = matrix_1d.reshape(matrix.shape[0], matrix.shape[1])


mult_matrix = np.multiply(matrix, matrix_2d)


sum_mult_matrix = np.sum(mult_matrix)


print(f"Original matrix: {matrix}")
print(f"Reshaped 1D array: {matrix_1d}")
print(f"Mean of 1D array: {mean_1d}")
print(f"Standard deviation of 1D array: {std_1d}")
print(f"Reshaped 2D matrix: {matrix_2d}")
print(f"Element-wise multiplied matrix: {mult_matrix}")
print(f"Sum of all elements in element-wise multiplied matrix: {sum_mult_matrix}")


x2 = "Creating new branch"
print(x2)