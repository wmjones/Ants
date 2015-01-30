from World import neighborhood
from display import graphHexGrid
from ants import Ant

n = 10
myWorld = []
myWorld = [[0 for j in range(n)] for i in range(n)]

# Ant.v(Ant(0))
# print myWorld
# print neighborhood(myWorld,*v)

numOfAnts = 1
population = []
for i in range(numOfAnts):
    population.append(Ant(i))
for t in range(8):
    graphHexGrid(500, 500, 10, myWorld, t)
    for i in range(len(population)):
        a, b = (population[i].p)[0], (population[i].p)[1]
        myWorld[a][b] = 1
        print population[i].p, neighborhood(myWorld, *population[i].p)
        z = Ant.look(population[i], *neighborhood(myWorld, *(population[i].p)))
        population[i].p = z

# myWorld[5][5]=1
# graphHexGrid(200,200,10,myWorld,1)
# myWorld[4][5]=1
# graphHexGrid(500,500,10,myWorld,2)
# myWorld[4][6]=1
# graphHexGrid(500,500,10,myWorld,3)
# myWorld[5][6]=1
# graphHexGrid(500,500,10,myWorld,4)
# myWorld[6][5]=1
# graphHexGrid(500,500,10,myWorld,5)
# myWorld[6][4]=1
# graphHexGrid(500,500,10,myWorld,6)
# myWorld[5][4]=1
# graphHexGrid(500,500,10,myWorld,7)
# print neighborhood(myWorld,*[5,5])
