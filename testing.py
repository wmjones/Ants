
class Agent:

    def __init__(self, i):
        # No real reason they are named/isnt used
        self.name = 'Agent' + str(i)

    def move(self, *neighborhood_list):
        # This function should take the neighborhood around a given agent and
        # then compute where to move, I kept this simple for the example. The
        # agent moves to the first cell that has 1 in a certain part of A
        # (i.e. if A[j][i][1] == 1)
        n = len(neighborhood_list)
        for i in range(n):
            if neighborhood_list[i][1] == 1:
                return i
            else:
                print 'Code wont get here in this Example'


def neighborhood(j, i):
    return A[j-1][i], A[j][i+1], A[j+1][i], A[j][i-1]
    # This is the cells to the left, above, to the right and then down with
    # respect to a given cell

# Here I create the Array
A = [[[[], []] for i in range(3)] for j in range(3)]
# A[Column][Row][0 for agents, 1 for integers][position after that (e.g. first
# agent in that list)]

# Here I am populating the array with 1 Agent in each row and column and 1 int
# for each row column (which is i + j)
for j in range(3):
    for i in range(3):
        A[j][i][0].append(Agent(i + j))
        A[j][i][1] = i + j
        # So ignoring the agents the int aspect is
        # [[0, 1, 2], [1, 2, 3], [2, 3, 4]] and so the int part of
        # neighborhood(1, 1) will be [1, 1, 3, 3]

print A[1][1][0][0]
# outputs <__main__.Agent instance at 0x10dfda950>
print A[1][1][0][0].move(*neighborhood(1, 1))
# outputs 0

# So I should move the agent from A[1][1]... to A[0][1]... (i.e. A[j-1][i])
A[0][1][0].append(A[1][1][0].pop(0))

print A[0][1]
# outputs [[<__main__.Agent instance at 0x10dfdae60>,
# <__main__.Agent instance at 0x10dfda878>], 1]
print A[1][1]
# outputs [[], 2]
