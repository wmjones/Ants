from World import neighborhood
#import __builtin__
# from display import graphHexGrid
from ants import Ant



n = 4
# __builtins__.myWorld = [[[] for j in range(n)] for i in range(n)]
myWorld = [[[] for j in range(n)] for i in range(n)]
numOfAnts = 1
myWorld[0][0] = [Ant(i) for i in range(numOfAnts)]
for t in range(1):
    #  graphHexGrid(500, 500, 10, myWorld[:, :], t)
    for col in range(n):
        for row in range(n):
            for ant in range(len(myWorld[col][row])):
                print neighborhood(myWorld, 0, 0)
                x = neighborhood(myWorld, 0, 0)[0]
                x = 2
                print neighborhood(myWorld, 0, 0)[0]
                print myWorld
                # N_ant = neighborhood(myWorld, col, row)
                # y, x = Ant.look(myWorld[col][row][ant], col, row, *N_ant)
                # print col, row, ant, x, y
                # print myWorld
                # myWorld[y][x].append(myWorld[col][row].pop(ant))
                # print myWorld[y][x][0]
                # print myWorld
print myWorld

# myWorld
#     neighborhood(myWorld)
#         ants(neighborhood(myWorld))
