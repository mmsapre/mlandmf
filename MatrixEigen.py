import numpy as np

def eigen(A):
    return np.linalg.eig(A)

def main():
    printopt = np.get_printoptions()
    np.set_printoptions(formatter={'float': '{:8.2f}'.format}, linewidth=200)

    # A = np.array([[-2, 2, -3],
    #                 [2, 1, -6],
    #                 [-1, -2, 0]])
    A = np.array([[80, 100, 40],
                  [100, 170 , 140],
                  [40, 140 , 200]])
    eigenvalue,eigenvector=eigen(A)
    print('eigenvalue = \n{}'.format(eigenvalue))
    print('eigenvector = \n{}'.format(eigenvector))
    v1 = eigenvector[:, 1].reshape(3, 1)
    v0 = eigenvector[:, 0].reshape(3, 1)
    # v2 = eigenvector[:, 2].reshape(3, 1)
    print('eigenvectors V1 = \n{}'.format(v1))
    print('eigenvectors V0 = \n{}'.format(v0))
    # print('eigenvectors V2 = \n{}'.format(v2))
if __name__ == '__main__':
    main()