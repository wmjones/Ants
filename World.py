# figure out how to pull in the actual myWorld[j][i] element not just a copy of it
def neighborhood(matrix, *arg):
    n = len(matrix)
    i, j = arg[1], arg[0]
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
