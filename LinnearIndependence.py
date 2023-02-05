import numpy as np

class LinearIndependence:
    # Initial default values
    A = [[7, 2, -3, 1 ,1], [-4, 8, 1, -2,1], [3, -2, 9, 2,1], [1, -1, 1, 4,1], [1, -1, 1, 4,1]]

    def gramschmidt(self):
        """ Gram-Schmidt orthogonalization of column-vectors. Matrix A passes
        vectors in its columns, orthonormal system is returned in columns of
        matrix Q. """
        _, k = self.A.shape
        GS=self.A
        # first basis vector
        Q = GS[:, [0]] / np.linalg.norm(GS[:, 0])
        for j in range(1, k):
            # orthogonal projection, loop-free implementation
            q = GS[:, j] - np.dot(Q, np.dot(Q.T, GS[:, j]))

            # check premature termination
            nq = np.linalg.norm(q)
            if nq < 1e-9 * np.linalg.norm(GS[:, j]):
                break
            # add new basis vector as another column of Q
            Q = np.column_stack([Q, q / nq])
        return Q

    def randomMatrixA(self):
        np.random.RandomState(400)
        randomA = np.random.uniform(-5.0, 5.0, size=(5, 5))
        self.A = randomA

    def isLinearIndependence(self):
        C=np.array(self.A).T
        return np.linalg.matrix_rank(C)==len(self.A)

    def transpose(self,u):
        result = [[u[j][i] for j in range(len(u))] for i in range(len(u[0]))]
        return result

    def forbenusNorm(self, a):
        forNorm = np.sqrt(np.sum(np.abs(a) ** 2))
        return forNorm

    def trunc(self,values, decs=0):
        return np.trunc(values * 10 ** decs) / (10 ** decs)

    def vectorTotest(self):
        return self.A

m = LinearIndependence()
m.randomMatrixA()
m.isLinearIndependence()
print("Linnear Independent vector :")
print("{:10}".format(np.array_str(m.vectorTotest(), precision=4, suppress_small=False)))
print()
print()
gs=m.gramschmidt()
print("Gram-Schimdt vector :")
print("{:10}".format(np.array_str(gs, precision=4, suppress_small=True)))
print()
print()
gsTrunc=m.trunc(gs,decs=2)
gsT=m.transpose(gsTrunc)
B=np.dot(gsTrunc,gsT)
print(" B = Q⊤Q. :")
print("{:10}".format(np.array_str(B, precision=4, suppress_small=True)))
print()
print()
bTrunc=m.trunc(B,decs=6)
I=np.identity(5)
newB=np.subtract(bTrunc,I)
fbNorm=m.forbenusNorm(newB)
print(" ∥B −I5∥F :",fbNorm)
