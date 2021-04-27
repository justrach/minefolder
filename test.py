# import numpy as np
# import scipy.linalg
# def diagonalize_unitary_using_two_orthogonals(u):
#     """Decomposes u into L @ np.diag(D) @ R.T where L and R are real orthogonal.
#     """
#     diag_r, diag_i, left, right = scipy.linalg.qz(np.real(u), np.imag(u))
#     diag = np.diagonal(diag_r) + np.diagonal(diag_i) * 1j
#     return left, diag, right

# u = np.array([[3,1,1,1],[1,3,1,1],[1,1,3,1],[1,1,1,3]])

# print(diagonalize_unitary_using_two_orthogonals(u))

from sympy import *
# init_printing()
A = Matrix(3,3,[5,-2,-4,-2,8,-2,-4,-2,5])
p=A.charpoly().as_expr()
factor(p)

x = A.nullspace()

print(x)