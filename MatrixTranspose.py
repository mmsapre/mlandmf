import numpy as np

def transpose(u):
    result = [[u[j][i] for j in range(len(u))] for i in range(len(u[0]))]
    return result

def main():
    printopt = np.get_printoptions()
    np.set_printoptions(formatter={'float': '{:8.3g}'.format}, linewidth=200)

    matrix = np.array([[1, 1, -1, 3, 0],
                    [3, 1, -1, -1, 0],
                    [2, -1, -2, 1, 0]])

    ut = transpose(matrix)
    print('matrix transpose = \n{}'.format(ut))



if __name__ == '__main__':
    main()