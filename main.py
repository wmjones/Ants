
#print setup.neighborhood(myWorld,1,1)

class AntSimulation:
    def _init_(self, gridSize, numAgents, Nmax):
        self.n = gridSize
        self.numAgents = numAgents
        self.Nmax = Nmax

    def generateWorld(self):
        self.myWorld=[]
        self.myWorld=[[0 for j in range(self.n)] for i in range(self.n)]
        
    def direction(self,i,j):
        neighborhood(i,j)
        #calculate weights of each neighboring cell
        #randomly choose cell based on weights
        return [k,l]
    
    def neighborhood(self,i,j):
        n=self.n
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

 #def _init_(self, i,j):
 #       self.position=[i,j]
 #       ant.antCount +=1
   
