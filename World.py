#myWorld=[['A','B','C'],['D','E','F'],['H','I','J']]



def neighborhood(myWorld,i,j):
    n=len(myWorld)
    cells=[]
    if i==0 and j==0 or i==n-1 and j==(n-1):
        cells.append(myWorld[n-2][n-2])
        cells.append(myWorld[n-2][n-1])
        cells.append(myWorld[0][1])
        cells.append(myWorld[1][1])
        cells.append(myWorld[1][0])
        cells.append(myWorld[n-1][n-2])
    elif i==0 and j==(n-1):
        cells.append(myWorld[n-1][j-1])
        cells.append(myWorld[n-1][j])
        cells.append(myWorld[i][0])
        cells.append(myWorld[i+1][0])
        cells.append(myWorld[i+1][j])
        cells.append(myWorld[i][j-1])
    elif i==0:
        cells.append(myWorld[n-1][j-1])
        cells.append(myWorld[n-1][j])
        cells.append(myWorld[i][j+1])
        cells.append(myWorld[i+1][j+1])
        cells.append(myWorld[i+1][j])
        cells.append(myWorld[i][j-1])
    elif i==(n-1):
        cells.append(myWorld[i-1][j-1])
        cells.append(myWorld[i-1][j])
        cells.append(myWorld[i][j+1])
        cells.append(myWorld[0][j+1])
        cells.append(myWorld[0][j])
        cells.append(myWorld[i][j-1])
    elif j==0 and i==(n-1):
        cells.append(myWorld[i-1][n-1])
        cells.append(myWorld[i-1][j])
        cells.append(myWorld[i][j+1])
        cells.append(myWorld[0][j+1])
        cells.append(myWorld[0][j])
        cells.append(myWorld[i][n-1])
    elif j==0: 
        cells.append(myWorld[i-1][n-1])
        cells.append(myWorld[i-1][j])
        cells.append(myWorld[i][j+1])
        cells.append(myWorld[i+1][j+1])
        cells.append(myWorld[i+1][j])
        cells.append(myWorld[i][n-1])
    elif j==(n-1):
        cells.append(myWorld[i-1][j-1])
        cells.append(myWorld[i-1][j])
        cells.append(myWorld[i][0])
        cells.append(myWorld[i+1][0])
        cells.append(myWorld[i+1][j])
        cells.append(myWorld[i][j-1])
    else:
        cells.append(myWorld[i-1][j-1])
        cells.append(myWorld[i-1][j])
        cells.append(myWorld[i][j+1])
        cells.append(myWorld[i+1][j+1])
        cells.append(myWorld[i+1][j])
        cells.append(myWorld[i][j-1])
    return cells

#for i in range(n):
#    for j in range(n):
#        print i,j
#        print neighborhood(i,j)

#i=2
#j=2
#myWorld[i-1][j-2]='F1A1'
#myWorld[i-2][j-2]='A1'
#myWorld[i-2][j-1]='A1B1'
#myWorld[i-2][j]='B1'
#myWorld[i-1][j+1]='B1C1'
#myWorld[i][j+2]='C1'
#myWorld[i+1][j+2]='C1D1'
#myWorld[i+2][j+2]='D1'
#myWorld[i+2][j+1]='D1E1'
#myWorld[i+2][j]='E1'
#myWorld[i+1][j-1]='E1F1'
#myWorld[i][j-2]='F1'

#print myWorld

#def neighborhood(i,j):
#    cells=[]
#    if i>=n-1 and j!=0 and j!=n-1:
#        cells.append(myWorld[0][j-1])
#        cells.append(myWorld[0][j-1])
#    elif i==0 and j!=0 and j!=n-1:
#        cells.append(myWorld[n-1][j-1])
#        cells.append(myWorld[n-1][j])
#    elif j==0:
#        cells.append(myWorld[i+1][n-1])
#        cells.append(myWorld[i-1][n-1])
#    elif j==n-1:
#        cells.append(myWorld[i][0])
#        cells.append(myWorld[i-1][0])
#    else:
#        print 'Error bad indexing'
#    
#    cells.append(myWorld[i][j+1])
#    cells.append(myWorld[i-1][j-1])
#    cells.append(myWorld[i-1][j])
#    cells.append(myWorld[i][j-1])
#    return cells
#print neighborhood(1,1)
