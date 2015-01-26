from World import neighborhood


n=2*5
nest=[n/2,n/2]
myWorld=[]
myWorld=[[0 for j in range(n)] for i in range(n)]

from ants import Ant

#Ant.v(Ant(0))
#print myWorld
#print neighborhood(myWorld,*v)

numOfAnts=10
population=[]
for i in range(numOfAnts):
    population.append(Ant(i))
print population

print population[0].p
Ant.look(population[0],*neighborhood(myWorld,*(population[0].p)))
print population[0].p
