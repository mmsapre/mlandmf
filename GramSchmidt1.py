import numpy as np

def gramschmidt(A):
    """ Gram-Schmidt orthogonalization of column-vectors. Matrix A passes
    vectors in its columns, orthonormal system is returned in columns of
    matrix Q. """
    _, k = A.shape

    # first basis vector
    Q = A[:, [0]] / np.linalg.norm(A[:, 0])
    for j in range(1, k):
        # orthogonal projection, loop-free implementation
        q = A[:, j] - np.dot(Q, np.dot(Q.T, A[:, j]))

        # check premature termination
        nq = np.linalg.norm(q)
        if nq < 1e-9 * np.linalg.norm(A[:, j]):
            break
        # add new basis vector as another column of Q
        Q = np.column_stack([Q, q / nq])
    return Q

def transposeForQ(q):
    for row in q:
        qt=[[round(q[j][i],3) for j in range(len(q))] for i in range(len(q[0]))]
    return qt
    # for i in range(len(q)):
    #     for j in range(len(q[i])):
    #         qt[i][j] = q[j][i]
    # return qt

def qrDecomposeR(qt,A):
    result = [[sum(round(a * b,2) for a, b in zip(X_row, Y_col)) for Y_col in zip(*A)] for X_row in qt]
    return result


def main():
    """ Main function, demonstrates roundoff on the result of the Gram-Schmidt
    orthogonalization. """
    # set print options to use lower precision
    printopt = np.get_printoptions()
    np.set_printoptions(formatter={'float': '{:8.4g}'.format}, linewidth=200)

    A = np.array([[1, 1, 2],
                  [1, 1, 0],
                  [1, 0, 0]])
    Q = gramschmidt(A)
    print('Q = \n{}'.format(Q))
    qt = transposeForQ(Q)
    print('QT = \n{}'.format(qt))
    r=qrDecomposeR(qt,A)
    print('r = \n{}'.format(r))
if __name__ == '__main__':
    main()
