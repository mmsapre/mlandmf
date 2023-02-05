import numpy as np

A = [[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19],
     [6,8,10,0]]
diagonal=np.diag(np.abs(A))

diff_diag=np.sum(np.abs(A),axis=1) - diagonal
print(diff_diag)
print(diagonal)

if np.all(diagonal> diff_diag):
    print("Matrix is diagonally dominant")
else:
    print("Matrix is not diagonally dominant")

