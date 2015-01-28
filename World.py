def neighborhood(matrix,*p):
    n = len(matrix)
    i,j = p[0],p[1]
    cells=[]
    if i==0 and j==0 or i==n-1 and j==(n-1):
        cells.append(matrix[n-2][n-2])
        cells.append(matrix[n-2][n-1])
        cells.append(matrix[0][1])
        cells.append(matrix[1][1])
        cells.append(matrix[1][0])
        cells.append(matrix[n-1][n-2])
    elif i==0 and j==(n-1):
        cells.append(matrix[n-1][j-1])
        cells.append(matrix[n-1][j])
        cells.append(matrix[i][0])
        cells.append(matrix[i+1][0])
        cells.append(matrix[i+1][j])
        cells.append(matrix[i][j-1])
    elif i==0:
        cells.append(matrix[n-1][j-1])
        cells.append(matrix[n-1][j])
        cells.append(matrix[i][j+1])
        cells.append(matrix[i+1][j+1])
        cells.append(matrix[i+1][j])
        cells.append(matrix[i][j-1])
    elif i==(n-1):
        cells.append(matrix[i-1][j-1])
        cells.append(matrix[i-1][j])
        cells.append(matrix[i][j+1])
        cells.append(matrix[0][j+1])
        cells.append(matrix[0][j])
        cells.append(matrix[i][j-1])
    elif j==0 and i==(n-1):
        cells.append(matrix[i-1][n-1])
        cells.append(matrix[i-1][j])
        cells.append(matrix[i][j+1])
        cells.append(matrix[0][j+1])
        cells.append(matrix[0][j])
        cells.append(matrix[i][n-1])
    elif j==0: 
        cells.append(matrix[i-1][n-1])
        cells.append(matrix[i-1][j])
        cells.append(matrix[i][j+1])
        cells.append(matrix[i+1][j+1])
        cells.append(matrix[i+1][j])
        cells.append(matrix[i][n-1])
    elif j==(n-1):
        cells.append(matrix[i-1][j-1])
        cells.append(matrix[i-1][j])
        cells.append(matrix[i][0])
        cells.append(matrix[i+1][0])
        cells.append(matrix[i+1][j])
        cells.append(matrix[i][j-1])
    else:
        cells.append(matrix[i-1][j-1])
        cells.append(matrix[i-1][j])
        cells.append(matrix[i][j+1])
        cells.append(matrix[i+1][j+1])
        cells.append(matrix[i+1][j])
        cells.append(matrix[i][j-1])
    return cells
#[i-1,j],[i-1,j+1],[i,j+1],[i+1,j],[i+1,j-1],[i,j-1]


#for i in range(n):
#    for j in range(n):
#        print i,j
#        print neighborhood(i,j)

#i=2
#j=2
#matrix[i-1][j-2]='F1A1'
#matrix[i-2][j-2]='A1'
#matrix[i-2][j-1]='A1B1'
#matrix[i-2][j]='B1'
#matrix[i-1][j+1]='B1C1'
#matrix[i][j+2]='C1'
#matrix[i+1][j+2]='C1D1'
#matrix[i+2][j+2]='D1'
#matrix[i+2][j+1]='D1E1'
#matrix[i+2][j]='E1'
#matrix[i+1][j-1]='E1F1'
#matrix[i][j-2]='F1'

#print matrix

#def neighborhood(i,j):
#    cells=[]
#    if i>=n-1 and j!=0 and j!=n-1:
#        cells.append(matrix[0][j-1])
#        cells.append(matrix[0][j-1])
#    elif i==0 and j!=0 and j!=n-1:
#        cells.append(matrix[n-1][j-1])
#        cells.append(matrix[n-1][j])
#    elif j==0:
#        cells.append(matrix[i+1][n-1])
#        cells.append(matrix[i-1][n-1])
#    elif j==n-1:
#        cells.append(matrix[i][0])
#        cells.append(matrix[i-1][0])
#    else:
#        print 'Error bad indexing'
#    
#    cells.append(matrix[i][j+1])
#    cells.append(matrix[i-1][j-1])
#    cells.append(matrix[i-1][j])
#    cells.append(matrix[i][j-1])
#    return cells
#print neighborhood(1,1)

#matrix=[['A','B','C'],['D','E','F'],['H','I','J']]
