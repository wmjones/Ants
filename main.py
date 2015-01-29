from World import neighborhood
from display import graphHexGrid

n=2*4
myWorld=[]
myWorld=[[0 for j in range(n)] for i in range(n)]

from ants import Ant

#Ant.v(Ant(0))
#print myWorld
#print neighborhood(myWorld,*v)

numOfAnts=3
population=[]
for i in range(numOfAnts):
    population.append(Ant(i))

for t in range(5):
    graphHexGrid(500,500,10,myWorld)
    for i in range(len(population)):
        a, b = (population[i].p)[0], (population[i].p)[1]
        myWorld[a][b]=1
        Ant.look(population[i],*neighborhood(myWorld,*(population[i].p)))
#myWorld[5][5]=1
#graphHexGrid(500,500,10,myWorld)
#myWorld[4][5]=1
#graphHexGrid(500,500,10,myWorld)
#myWorld[5][6]=1
#graphHexGrid(500,500,10,myWorld)
#myWorld[6][6]=1
#graphHexGrid(500,500,10,myWorld)
#myWorld[6][5]=1
#graphHexGrid(500,500,10,myWorld)
#myWorld[5][4]=1
#graphHexGrid(500,500,10,myWorld)
#myWorld[4][4]=1
#graphHexGrid(500,500,10,myWorld)

print myWorld
