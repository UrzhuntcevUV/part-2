import numpy as np

N = 4
M = 5

K = 2


matrix = np.random.randint(low=-9, high=10, size=(N, M))
print("Матрица:\r\n{}".format(matrix))

matrix = np.delete(matrix, K, axis=1)
print("Полученная матрица:\r\n {}".format(matrix))
