import numpy as np


def nbrhdIndexs(i, j, n):
    if (i == 0 and j == n-1) or (i == (n-1) and j == 0):
        return np.array([(0, n-2), (1, n-2), (1, n-1),
                         (n-1, 1), (n-2, 1), (n-2, 0)])
        # myWorld[0][n-2] = args[0]
        # myWorld[1][n-2] = args[1]
        # myWorld[1][n-1] = args[2]
        # myWorld[n-1][1] = args[3]
        # myWorld[n-2][1] = args[4]
        # myWorld[n-2][0] = args[5]
    elif i == 0 and j == 0:
        return np.array([(0, n-1), (1, n-1), (1, 0),
                         (0, 1), (n-1, 1), (n-1, 0)])
#        myWorld[1][n-1] = args[1]
#        myWorld[1][0] = args[2]
#        myWorld[0][1] = args[3]
#        myWorld[n-1][1] = args[4]
#        myWorld[n-1][0] = args[5]
    elif j == (n-1) and i == (n-1):
        return np.array([(n-1, n-2), (0, n-2), (0, n-1),
                         (n-1, 0), (n-2, 0), (n-2, n-1)])
#        myWorld[n-1][n-2] = args[0]
#        myWorld[0][n-2] = args[1]
#        myWorld[0][n-1] = args[2]
#        myWorld[n-1][0] = args[3]
#        myWorld[n-2][0] = args[4]
#        myWorld[n-2][n-1] = args[5]
    elif i == 0:
        return np.array([(j, n-1), (j+1, n-1), (j+1, 0),
                         (j+1, 1), (j, 1), (j-1, 0)])
#        myWorld[j][n-1] = args[0]
#        myWorld[j+1][n-1] = args[1]
#        myWorld[j+1][0] = args[2]
#        myWorld[j+1][1] = args[3]
#        myWorld[j][1] = args[4]
#        myWorld[j-1][0] = args[5]
    elif i == (n-1):
        return np.array([(j, i-1), (j+1, i-1), (j+1, i),
                         (j, 0), (j-1, 0), (j-1, i)])
#        myWorld[j][i-1] = args[0]
#        myWorld[j+1][i-1] = args[1]
#        myWorld[j+1][i] = args[2]
#        myWorld[j][0] = args[3]
#        myWorld[j-1][0] = args[4]
#        myWorld[j-1][i] = args[5]
    elif j == 0:
        return np.array([(j, i-1), (j+1, i-1), (j+1, i),
                         (j, i+1), (n-1, i+1), (n-1, i)])
#        myWorld[j][i-1] = args[0]
#        myWorld[j+1][i-1] = args[1]
#        myWorld[j+1][i] = args[2]
#        myWorld[j][i+1] = args[3]
#        myWorld[n-1][i+1] = args[4]
#        myWorld[n-1][i] = args[5]
    elif j == (n-1):
        return np.array([(j, i-1), (0,  i-1), (0, i),
                         (j, i+1), (j-1, i+1), (j-1, i)])
#        myWorld[j][i-1] = args[0]
#        myWorld[0][i-1] = args[1]
#        myWorld[0][i] = args[2]
#        myWorld[j][i+1] = args[3]
#        myWorld[j-1][i+1] = args[4]
#        myWorld[j-1][i] = args[5]
    else:
        return np.array([(j, i-1), (j+1, i-1), (j+1, i),
                         (j, i+1), (j-1, i+1), (j-1, i)])
#        myWorld[j][i-1] = args[0]
#        myWorld[j+1][i-1] = args[1]
#        myWorld[j+1][i] = args[2]
#        myWorld[j][i+1] = args[3]
#        myWorld[j-1][i+1] = args[4]
#        myWorld[j-1][i] = args[5]


def getNeighborhood(matrix,  j,  i,  *args):
    n = len(matrix)
    cells = []
    if (i == 0 and j == n-1) or (i == (n-1) and j == 0):
        cells.append(matrix[0][n-2])
        cells.append(matrix[1][n-2])
        cells.append(matrix[1][n-1])
        cells.append(matrix[n-1][1])
        cells.append(matrix[n-2][1])
        cells.append(matrix[n-2][0])
    elif i == 0 and j == 0:
        cells.append(matrix[0][n-1])
        cells.append(matrix[1][n-1])
        cells.append(matrix[1][0])
        cells.append(matrix[0][1])
        cells.append(matrix[n-1][1])
        cells.append(matrix[n-1][0])
    elif j == (n-1) and i == (n-1):
        cells.append(matrix[n-1][n-2])
        cells.append(matrix[0][n-2])
        cells.append(matrix[0][n-1])
        cells.append(matrix[n-1][0])
        cells.append(matrix[n-2][0])
        cells.append(matrix[n-2][n-1])
    elif i == 0:
        cells.append(matrix[j][n-1])
        cells.append(matrix[j+1][n-1])
        cells.append(matrix[j+1][0])
        cells.append(matrix[j+1][1])
        cells.append(matrix[j][1])
        cells.append(matrix[j-1][0])
    elif i == (n-1):
        cells.append(matrix[j][i-1])
        cells.append(matrix[j+1][i-1])
        cells.append(matrix[j+1][i])
        cells.append(matrix[j][0])
        cells.append(matrix[j-1][0])
        cells.append(matrix[j-1][i])
    elif j == 0:
        cells.append(matrix[j][i-1])
        cells.append(matrix[j+1][i-1])
        cells.append(matrix[j+1][i])
        cells.append(matrix[j][i+1])
        cells.append(matrix[n-1][i+1])
        cells.append(matrix[n-1][i])
    elif j == (n-1):
        cells.append(matrix[j][i-1])
        cells.append(matrix[0][i-1])
        cells.append(matrix[0][i])
        cells.append(matrix[j][i+1])
        cells.append(matrix[j-1][i+1])
        cells.append(matrix[j-1][i])
    else:
        cells.append(matrix[j][i-1])
        cells.append(matrix[j+1][i-1])
        cells.append(matrix[j+1][i])
        cells.append(matrix[j][i+1])
        cells.append(matrix[j-1][i+1])
        cells.append(matrix[j-1][i])
    return cells
