import numpy as np

N = 4


A = np.random.randint(low=-9, high=10, size=(N, N))
print("Матрица:\r\n{}".format(A))

diagonal_elements = np.array([np.diagonal(A[::-1], i) for i in [1, -1]]).flatten()
print("Элементы, расположенные параллельно побочной диагонали:")
print(diagonal_elements)

print("Сумма элементов, расположенные параллельно побочной диагонали:")
print(np.prod(diagonal_elements))
