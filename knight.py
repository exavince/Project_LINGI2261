# -*-coding: utf-8 -*
'''NAMES OF THE AUTHOR(S): Gael Aglin <gael.aglin@uclouvain.be>'''
import time
import sys
import copy
from search import *


#################
# Problem class #
#################
class Knight(Problem):

    def successor(self, state):
        row, col = state.position
        print(state.counter)
        print(state.position)
        if row - 1 >= 0:
            if col - 2 >= 0 and checkPosition(state, row - 1, col - 2):
                newState = copy.deepcopy(state)
                newState.grid[row][col] = "\u265E"
                newState.grid[row - 1][col - 2] = "♘"
                newState.position = (row - 1, col - 2)
                newState.counter = state.counter - 1
                yield ("", newState)
            if col + 2 < state.nCols and checkPosition(state, row - 1, col + 2):
                newState = copy.deepcopy(state)
                newState.grid[row][col] = "\u265E"
                newState.grid[row - 1][col + 2] = "♘"
                newState.position = (row - 1, col + 2)
                newState.counter = state.counter - 1
                yield ("", newState)
        if row + 1 < state.nRows:
            if col - 2 >= 0 and checkPosition(state, row + 1, col - 2):
                newState = copy.deepcopy(state)
                newState.grid[row][col] = "\u265E"
                newState.grid[row + 1][col - 2] = "♘"
                newState.position = (row + 1, col - 2)
                newState.counter = state.counter - 1
                yield ("", newState)
            if col + 2 < state.nCols and checkPosition(state, row + 1, col + 2):
                newState = copy.deepcopy(state)
                newState.grid[row][col] = "\u265E"
                newState.grid[row + 1][col + 2] = "♘"
                newState.position = (row + 1, col + 2)
                newState.counter = state.counter - 1
                yield ("", newState)
        if col - 1 >= 0:
            if row - 2 >= 0 and checkPosition(state, row - 2, col - 1):
                newState = copy.deepcopy(state)
                newState.grid[row][col] = "\u265E"
                newState.grid[row - 2][col - 1] = "♘"
                newState.position = (row - 2, col - 1)
                newState.counter = state.counter - 1
                yield ("", newState)
            if row + 2 < state.nRows and checkPosition(state, row + 2, col - 1):
                newState = copy.deepcopy(state)
                newState.grid[row][col] = "\u265E"
                newState.grid[row + 2][col - 1] = "♘"
                newState.position = (row + 2, col - 1)
                newState.counter = state.counter - 1
                yield ("", newState)
        if col + 1 < state.nCols:
            if row - 2 >= 0 and checkPosition(state, row - 2, col + 1):
                newState = copy.deepcopy(state)
                newState.grid[row][col] = "\u265E"
                newState.grid[row - 2][col + 1] = "♘"
                newState.position = (row - 2, col + 1)
                newState.counter = state.counter - 1
                yield ("", newState)
            if row + 2 < state.nRows and checkPosition(state, row + 2, col + 1):
                newState = copy.deepcopy(state)
                newState.grid[row][col] = "\u265E"
                newState.grid[row + 2][col + 1] = "♘"
                newState.position = (row + 2, col + 1)
                newState.counter = state.counter - 1
                yield ("", newState)

    def goal_test(self, state):
        return state.counter == 1


###############
# State class #
###############

class State:
    def __init__(self, shape, init_pos):
        self.nCols = shape[0]
        self.nRows = shape[1]
        self.position = init_pos
        self.counter = self.nCols * self.nRows
        self.grid = []
        for i in range(self.nRows):
            self.grid.append([" "] * self.nCols)
        self.grid[init_pos[0]][init_pos[1]] = "♘"

    def __str__(self):
        nsharp = (2 * self.nCols) + (self.nCols // 5)
        s = "#" * nsharp
        s += "\n"
        for i in range(self.nRows):
            s = s + "#"
            for j in range(self.nCols):
                s = s + str(self.grid[i][j]) + " "
            s = s[:-1]
            s = s + "#"
            if i < self.nRows - 1:
                s = s + '\n'
        s += "\n"
        s += "#" * nsharp
        return s


###################
# Other functions #
###################
def checkPosition(state, x, y):
    if state.grid[x][y] == " ":
        return True
    return False


##############################
# Launch the search in local #
##############################
# Use this block to test your code in local
# Comment it and uncomment the next one if you want to submit your code on INGInious


# with open('instancesFile') as f:
#     instances = f.read().splitlines()
#
# for instance in instances:
#     elts = instance.split(" ")
#     print(elts[0], elts[1])
#     shape = (int(elts[0]), int(elts[1]))
#     init_pos = (int(elts[2]), int(elts[3]))
#     init_state = State(shape, init_pos)
#
#     problem = Knight(init_state)
#
#     # example of bfs graph search
#     startTime = time.perf_counter()
#     node, nbExploredNodes = breadth_first_tree_search(problem)
#     endTime = time.perf_counter()
#
#     # example of print
#     path = node.path()
#     for n in path:
#         print(n)
#     path.reverse()
#
#     print('Number of moves: ' + str(node.depth))
#
#     print("nb nodes explored = ", nbExploredNodes)
#     print("time : " + str(endTime - startTime))

####################################
# Launch the search for INGInious  #
####################################
# Use this block to test your code on INGInious


shape = (int(sys.argv[1]),int(sys.argv[2]))
init_pos = (int(sys.argv[3]),int(sys.argv[4]))
init_state = State(shape, init_pos)

problem = Knight(init_state)

#        #example of bfs
startTime = time.perf_counter()
node, nbExploredNodes = breadth_first_graph_search(problem)
endTime = time.perf_counter()

#        #path = node.path()
path.reverse()

print('Number of moves: ' + str(node.depth))
for n in path:
    print(n.state)  # assuming that the __str__ function of state outputs the correct format
    print()
print("nb nodes explored = ",nbExploredNodes)
print("time : " + str(endTime - startTime))
