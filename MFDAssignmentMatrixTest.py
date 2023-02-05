import numpy as np
class MFDAssignmentMatrixTest:
    A = [[7, 2, -3, 1], [-4, 8, 1, -2], [3, -2, 9, 2], [1, -1, 1, 4]]
    B = [-1, 16, -3, 5]

    def randomMatrixAAndB(self):
        np.random.RandomState(400)
        randomA = np.random.uniform(-5.0, 5.0, size=(4, 4))
        self.A = randomA
        randomB = np.random.normal(loc=0, scale=1, size=4)
        self.B = randomB

    def diagonalDominant(self, a):
        diagonal = np.diag(np.abs(a))
        diff_diag = np.sum(np.abs(a), axis=1) - diagonal
        if np.all(diagonal > diff_diag):
            return 1
        else:
            return 0

m = MFDAssignmentMatrixTest()
m.randomMatrixAAndB()
matrixTest = m.diagonalDominant(m.A)
while matrixTest == 0:
    m.randomMatrixAAndB()
    matrixTest = m.diagonalDominant(m.A)

if matrixTest:
    print("Diagonally Dominant Input Matrix :{}".format(m.A))
    print("Considered B on RHS  :{}".format(m.B))
else:
    print("Matrix is not diagonally dominant")
