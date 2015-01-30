import random


class Ant:

    def __init__(self, name):
        self.name = 'Ant' + str(name)

    def look(self, j, i, *Neighborhood):
        probabilities = []
        probabilities = [.1667, 2*.1667, 3*.1667, 4*.1667, 5*.1667, 6*.1667]
        x = random.random()
        if x > probabilities[4]:
            y_cordinate, x_cordinate = j, i-1
        elif x > probabilities[3]:
            y_cordinate, x_cordinate = j+1, i-1
        elif x > probabilities[2]:
            y_cordinate, x_cordinate = j+1, i
        elif x > probabilities[1]:
            y_cordinate, x_cordinate = j, i+1
        elif x > probabilities[0]:
            y_cordinate, x_cordinate = j-1, i+1
        else:
            y_cordinate, x_cordinate = j-1, i
        return y_cordinate, x_cordinate
