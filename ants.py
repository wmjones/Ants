import random


class Ant:

    nest = [1, 1]

    def __init__(self, name):
        self.p = Ant.nest
        self.name = 'Ant' + str(name)

    def look(self, j, i, *Neighborhood):
        # Calculates weights for each neighboring cell then uses
        # a cumlative distribution to determine which cell to
        # move to
        # N_ant = map(float, Neighborhood)
        # total = sum(N_ant)
        probabilities = []
        # if total >1000:
        #     for i in range(6):
        #         probabilities.append(N_ant[i]/total)
        #         #probabilities = [N_ant[i]/total for i in range(6)]
        #     for i in range(len(probabilities)):
        #         j=0
        #         while j<i:
        #             probabilities[i]+=probabilities[j]
        #             j+=1
        # else:
        probabilities = [.1667, 2*.1667, 3*.1667, 4*.1667, 5*.1667, 6*.1667]
        # change, so that I dont define cell just use neighborhood
        x = random.random()
        # i, j = self.p[0], self.p[1]
        if x > probabilities[4]:
            y_cordinate, x_cordinate = i-1, j
        elif x > probabilities[3]:
            y_cordinate, x_cordinate = i-1, j+1
        elif x > probabilities[2]:
            y_cordinate, x_cordinate = i, j+1
        elif x > probabilities[1]:
            y_cordinate, x_cordinate = i+1, j
        elif x > probabilities[0]:
            y_cordinate, x_cordinate = i+1, j-1
        else:
            y_cordinate, x_cordinate = i, j-1
        return i, j
