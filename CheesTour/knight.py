# -*-coding: utf-8 -*
'''NAMES OF THE AUTHOR(S): Gael Aglin <gael.aglin@uclouvain.be>'''
import time
import sys
import copy
from search import *
import cProfile

moves = [(-1, -2), (-1, +2), (1, -2), (1, +2), (-2, -1), (-2, +1), (2, -1), (2, +1)]  # initialized only once

#################
# Problem class #
#################
class Knight(Problem):
    def successor(self, state):
        col, row = state.position
        successors = []
        for move in moves:
            newCol, newRow = col + move[0], row + move[1]
            if validMove(self, state, newCol, newRow):
                newState = State((state.nCols, state.nRows), state.position)
                newState.grid = [list(x) for x in state.grid]
                newState.counter = state.counter - 1
                newState.grid[col][row] = "\u265E"
                newState.grid[newCol][newRow] = "♘"
                newState.position = (newCol, newRow)
                newState.numberSuccessors = numberSuccessors(self, state, newCol, newRow)
                successors.append(("", newState))
        return successors

    def goal_test(self, state):
        return state.counter == 1


###################
# Other functions #
###################
def validMove(self, state, col, row):
    return 0 <= col < state.nCols and 0 <= row < state.nRows and state.grid[col][row] == " "

def numberSuccessors(self, state, col, row):
    counter = 0
    for move in moves:
        newCol, newRow = col + move[0], row + move[1]
        if validMove(self, state, newCol, newRow): counter+= 1
    return counter

###############
# State class #
###############

class State:
    def __init__(self, shape, init_pos):
        self.nCols = shape[0]
        self.nRows = shape[1]
        self.grid = []
        self.position = init_pos
        self.counter = self.nCols * self.nRows
        self.numberSuccessors = 0
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


inginious = False

if not inginious:

    ##############################
    # Launch the search in local #
    ##############################
    # Use this block to test your code in local
    # Comment it and uncomment the next one if you want to submit your code on INGInious

    with open('instancesFile') as f:
        instances = f.read().splitlines()
        count = 0
        for instance in instances:
            elts = instance.split(" ")
            shape = (int(elts[0]), int(elts[1]))
            init_pos = (int(elts[2]), int(elts[3]))
            init_state = State(shape, init_pos)

            problem = Knight(init_state)
            print('Instance: ' + str(count))
            # example of bfs graph search

            startTime = time.perf_counter()
            node, nbExploredNodes = depth_first_graph_search(problem)
            endTime = time.perf_counter()

            count = count+1
            print('Number of moves: ' + str(node.depth))
            print("nb nodes explored = ", nbExploredNodes)
            print("time : " + str(endTime - startTime))

else:

    ####################################
    # Launch the search for INGInious  #
    ####################################
    # Use this block to test your code on INGInious

    shape = (int(sys.argv[1]), int(sys.argv[2]))
    init_pos = (int(sys.argv[3]), int(sys.argv[4]))
    init_state = State(shape, init_pos)

    problem = Knight(init_state)

    #        #example of bfs
    startTime = time.perf_counter()
    node, nbExploredNodes = depth_first_tree_search(problem)
    endTime = time.perf_counter()

    path = node.path()
    path.reverse()

    print('Number of moves: ' + str(node.depth))
    for n in path:
        print(n.state)  # assuming that the __str__ function of state outputs the correct format
        print()
    print("nb nodes explored = ", nbExploredNodes)
    print("time : " + str(endTime - startTime))
