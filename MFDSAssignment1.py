import numpy as np
import matplotlib.pyplot as plt


class MFDAssignment1:
    A = [[7, 2, -3, 1], [-4, 8, 1, -2], [3, -2, 9, 2], [1, -1, 1, 4]]
    B = [-1, 16, -3, 5]
    ITERATION_LIMIT = 25

    def randomMatrixAAndB(self):
        np.random.RandomState(400)
        randomA = np.random.uniform(-5.0, 5.0, size=(4, 4))
        self.A = randomA
        randomB = np.random.normal(loc=0, scale=1, size=4)
        self.B = randomB

    # def isDDM(self, a):
    #     n = len(a)
    #     for i in range(0, n):
    #         sum = 0
    #         for j in range(0, n):
    #             sum = sum + abs(a[i][j])
    #         sum = sum - abs(a[i][i])
    #         if (abs(a[i][i]) < sum):
    #             return False
    #     return True

    def diagonalDominant(self, a):
        diagonal = np.diag(np.abs(a))
        diff_diag = np.sum(np.abs(a), axis=1) - diagonal
        if np.all(diagonal > diff_diag):
            return 1
        else:
            return 0

    def norm1(self, a):
        norm1 = np.max(np.sum(np.abs(a), axis=0))
        return norm1

    def normInfinity(self, a):
        normInfinity = np.max(np.sum(np.abs(a), axis=1))
        return normInfinity

    def forbenusNorm(self, a):
        forNorm = np.sqrt(np.sum(np.abs(a) ** 2))
        return forNorm

    def siedel(self, a, x, b):
        n = len(a)

        for j in range(0, n):
            d = b[j]
            for i in range(0, n):
                if (j != i):
                    d -= a[j][i] * x[i]
            x[j] = d / a[j][j]
        return x

    def jacobi(self, a, x, b, tolerance=1e-10, max_iterations=100):
        tol=1.0e-4
        d = np.diag(a)
        r = a - np.diagflat(d)
        error_of_norn = []
        xold = x
        for i in range(max_iterations):
            r=(b - np.dot(r, x))
            x = r / d
            print("Iteration {0} : {1}".format(i, x))
            error = np.linalg.norm(x - xold)
            xold = x
            error_of_norn.append(error)
            print("Norm1 = %e \t; Normal Infinities = %e \t; Forbeneus = %e" % (
                np.linalg.norm(np.array(xold)), error,m.forbenusNorm(x)))

            # print("Norm1 = %e \t; " % (
            #     np.linalg.norm(r)))
        # return x
        plt.plot(range(1, 101), error_of_norn, color='r')
        plt.title("Gauss-Jaobi")
        plt.xlabel('Iterations')
        plt.ylabel('||Xk+1-Xk||2')
        plt.show()

    def gaussJacobi(self, a, b, tolerance=1e-10, max_iterations=10):
        error_of_norn = []
        print(a)
        n = len(a)
        print(n)
        x0 = np.array([0, 0, 0, 0])
        xnext = x0
        for iteration in range(max_iterations):
            for i in range(n):
                sigmaSum = 0
                for j in range(n):
                    if i != j:
                        sigmaSum = sigmaSum + a[i, j] * x0[j]
                xnext[i] = (b[i] - sigmaSum) / a[i, i]
            error = np.linalg.norm(xnext - x0)
            error_of_norn.append(error)
            x0 = xnext
            print("Solution of iteration", iteration, "\n", xnext);
            print("Norm1 = %e \t; Normal Infinities = %e \t; Forbeneus = %e" % (
                np.linalg(x0), np.linalg.norm(error, np.inf), self.forbenusNorm(error)))
        print("\n")
        print('Final iteration after 10 iteration is: \n', xnext)
        print("\n")
        # Let's plot the final result
        plt.plot(range(1, 11), error_of_norn, color='r')
        plt.xlabel('Iterations')
        plt.ylabel('||Xk+1-Xk||2')
        plt.show()


m = MFDAssignment1()
m.randomMatrixAAndB()
matrixTest = m.diagonalDominant(m.A)
#matrixTest1 = m.isDDM(m.A)
while matrixTest == 0:
    m.randomMatrixAAndB()
    matrixTest = m.diagonalDominant(m.A)

if matrixTest:
    print("Diagonally Dominant Input Matrix :{}".format(m.A))
    print("Considered B on RHS  :{}".format(m.B))
else:
    print("Matrix is not diagonally dominant")

normtest1 = m.norm1(m.A)
print(" Norm 1 for matrix:", normtest1)
normInfinities = m.normInfinity(m.A)
print("Infinity norm for matrix:", normInfinities)
normFor = m.forbenusNorm(m.A)
print("Forbenus norm:", normFor)
print(" -------------- Gauss Siedel -------------------------")
corord = [0, 0, 0, 0]
corordOld = corord
siedelError = []
for i in range(0, 100):
    corord = m.siedel(m.A, corord, m.B)
    print("Iteration  {0} : {1}".format(i, corord))
    error = np.linalg.norm(np.array(corord) - np.array(corordOld))
    siedelError.append(error)
    corordOld = corord
    print("Norm1 = %e \t; Normal Infinities = %e \t; Forbeneus = %e" % (
        np.linalg.norm(corord), np.linalg.norm(corord,np.inf), m.forbenusNorm(error)))
plt.plot(range(1, 101), siedelError, color='r')
plt.title("Gauss-Siedel")
plt.xlabel('Iterations')
plt.ylabel('||Xk+1-Xk||2')
plt.show()
print(" -------------- Gauss Jacobi  -------------------------")
initialX = np.array([0, 0, 0, 0])
print(m.jacobi(m.A, initialX, m.B, m.ITERATION_LIMIT))
