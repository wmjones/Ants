from World import neighborhood
# from display import graphHexGrid
from ants import Ant


class Main:
    n = 4
    myWorld = [[[] for j in range(n)] for i in range(n)]
    numOfAnts = 1
    myWorld[2][2] = [Ant(i) for i in range(numOfAnts)]
    for t in range(10):
        #  graphHexGrid(500, 500, 10, myWorld[:, :], t)
        for col in range(n):
            for row in range(n):
                for ant in range(len(myWorld[col][row])):
                    N_ant = neighborhood(myWorld, col, row)
                    y, x = Ant.look(myWorld[col][row][ant], col, row, *N_ant)
                    print col, row, ant, x, y
                    print myWorld
                    myWorld[y][x].append(myWorld[col][row].pop(ant))
                    print myWorld[y][x][0]
                    print myWorld
Main()
