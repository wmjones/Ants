
n=3;

myWorld=[]
myWorld=[[0 for j in range(n)] for i in range(n)]

def neighborhood(i,j):
    cells=[]
    if i>=n-1 and j!=0 and j!=n-1:
        cells.append(myWorld[0][j-1])
        cells.append(myWorld[0][j-1])
    elif i==0 and j!=0 and j!=n-1:
        cells.append(myWorld[n-1][j-1])
        cells.append(myWorld[n-1][j])
    elif j==0:
        cells.append(myWorld[i+1][n-1])
        cells.append(myWorld[i-1][n-1])
    elif j==n-1:
        cells.append(myWorld[i][0])
        cells.append(myWorld[i-1][0])
    else:
        print 'Error bad indexing'
    
    cells.append(myWorld[i][j+1])
    cells.append(myWorld[i-1][j-1])
    cells.append(myWorld[i-1][j])
    cells.append(myWorld[i][j-1])
    return cells
print neighborhood(1,1)
