import numpy as np
# from World import neighborhood
# import __builtin__
# from display import graphHexGrid
# from ants import Ant


def main(size_, t_, nAnt_):
    myWorld = np.zeros((size_, size_, 1))
    myWorld[1][1][0] = 1

    def pipeline(data, fns):
        # (myWorld, fns)
        return reduce(lambda a, x: x(a),
                      fns,
                      data)

    def move(x):
        return x + 1

    def move2(x):
        return x+2

    npmove = np.frompyfunc(lambda x: x+1, 1, 1)
    npmove2 = np.frompyfunc(move2, 1, 1)

    myWorld = pipeline(myWorld, [npmove, npmove2])
    print myWorld[1][1][0]

    # pipeline(myWorld, [move(myWorld)])
    # print myWorld

main(3, 1, 1)

# for t in range(1):
#     #  graphHexGrid(500, 500, 10, myWorld[:, :], t)
#     for col in range(n):
#         for row in range(n):
#             for ant in range(len(myWorld[col][row])):
#                 # N_ant = neighborhood(myWorld, col, row)
#                 # y, x = Ant.look(myWorld[col][row][ant], col, row, *N_ant)
#                 # print col, row, ant, x, y
#                 # print myWorld
#                 # myWorld[y][x].append(myWorld[col][row].pop(ant))
#                 # print myWorld[y][x][0]
#                 # print myWorld

# myWorld
#     neighborhood(myWorld)
#         ants(neighborhood(myWorld))
