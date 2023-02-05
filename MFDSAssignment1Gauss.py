import numpy as np
import numpy.linalg as la
import time


def GaussSeidel(A, b):
    # dimension of the non-singular matrix
    n = len(A)

    # def. max iteration and criterions
    Kmax = 100;
    tol = 1.0e-4;
    btol = la.norm(b) * tol

    x0 = np.zeros(n)
    k = 0;
    stop = False
    x1 = np.empty(n)

    while not (stop) and k < Kmax:
        print("begin while with k =", k)
        x1 = np.zeros(n)
        for i in range(n):  # rows of A
            x1[i] = (b[i] - np.dot(A[i, 0:i], x1[0:i]) - np.dot(A[i, i + 1:n], x0[i + 1:n])) / A[i, i]
            print("x1 =", x1)

        r = b - np.dot(A, x1)
        stop = (la.norm(r) < btol) and (la.norm(x1 - x0) < tol)
        print("end of for i \n")
        print("x0 =", x0)
        print("btol = %e \t; la.norm(r) = %e \t; tol = %e \t; la.norm(x1-x0) = %e; stop = %s " % (
        btol, la.norm(r), tol, la.norm(x1 - x0), stop))
        x0 = x1
        print("x0 =", x0, end='\n')
        print("end of current while \n\n")
        k = k + 1

    if not (stop):  # or if k >= Kmax
        print('Not converges in %d iterations' % Kmax)

    return x1, k


A = np.array([[3, -0.1, -0.2], [0.1, 7, -0.3], [0.3, -0.2, 10]], dtype='f')

b = np.array([7.85, -19.3, 71.4])

xsol = la.solve(A, b)

start = time.time()
x, k = GaussSeidel(A, b)
ending = time.time()
duration = ending - start
err = la.norm(xsol - x)
print('Iter.=%d  duration=%f  err=%e' % (k, duration, err))