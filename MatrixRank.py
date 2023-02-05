import numpy as np

def pythonRank(A):
    return np.linalg.matrix_rank(A)

def Displaymatrix(A, rownum, colnum):
    for i in range(rownum):
        for j in range(colnum):
            print(A)
            break


def swapRows(A, row1, row2):  # FUNCTION TO SWAP TWO ROWS OF A MATRIX A
    A[row2], A[row1] = A[row1], A[row2]
    return A


def Row_Transformation(A, x, row1, row2):  # FUNCTION TO PERFORM ROW TRANSFORMATION ON ROWS OF A MATRIX
    k = len(A[row2])
    for m in range(k):
        A[row2][m] = A[row2][m] + A[row1][m] * x
    return A


def MatrixRank(A):
    colnum = len(A[0])
    rownum = len(A)
    Rank = min(colnum, rownum)  # RANK IS THE MINIMUM OF colnum AND rownum
    if (rownum > colnum):
        list1 = []
        for i in range(colnum):
            list2 = []
            for j in range(rownum):
                list2.append(A[i][j])
            list1.append(list2)
        list1 = list2
        colnum, rownum = rownum, colnum

    for l in range(Rank):
        if (A[l][l] != 0):
            for n in range(l + 1, rownum):
                A = Row_Transformation(A, -(A[n][l] // A[l][l]), l, n)  # INVOKING Row_Transformation FUNCTION
        else:
            flag1 = True
            for o in range(l + 1, rownum):
                if (A[o][l] != 0):
                    A = swapRows(A, l, o)
                    flag1 = False
                    break
            if (flag1):
                for i in range(rownum):
                    A[i][l], A[i][Rank - 1] = A[i][Rank - 1], A[i][l]
            rownum = rownum - 1
        c = 0
        for z in A:
            if (z == [0] * colnum):
                c = c + 1
    return Rank - c
    print(Rank - c)


if __name__ == '__main__':

    matrix = np.array([[-2, 2, -3],
                    [2, 1, -6],
                    [-1, -2, 0]])

    # matrix = np.array([[3, 0],
    #                    [4, 5]])

    print(pythonRank(matrix))
    print(MatrixRank([[-2, 2, -3],
                    [2, 1, -6],
                    [-1, -2, 0]]))
