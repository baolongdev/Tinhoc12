# import numpy as np
# A = np.array([[4,0,5], [-1,3,2]])
# B = np.array([[1,1,1], [3,5,7]])
# C = np.array([[2,-3], [0,1]])
# # result = np.dot(A.T, A)
# print(A+B)
# print(A-B)
# print(2*A)
# print(-3*B)
# print(2*A-3*B)
# print(np.dot(A.T, C))
# print(np.dot(C, A) + B)
# print(np.dot(C, A).T - (2*B).T)

import numpy as np

def matrix_power(A, n):
    if n < 0:
        raise ValueError("Exponent n must be non-negative")
    if n == 0:
        return np.identity(A.shape[0])  # Ma trận đơn vị
    else:
        return np.linalg.matrix_power(A, n)

A = np.array([[1,2,1], [0,1,2], [3,1,1]])
print(matrix_power(A, 2))