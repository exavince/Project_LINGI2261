# -*-coding: utf-8 -*
'''NAMES OF THE AUTHOR(S): Gael Aglin <gael.aglin@uclouvain.be>'''
import time
from search import *

#################
# Problem class #
#################
class Pacmen(Problem):

    def successor(self, state):
        # Find where is the player
        pac_list = []
        action_list = []
        state_list = [state]

        for r in range(0, state.nbr):
            for c in range(0, state.nbc):
                if state.grid[r][c] == '$':
                    pac_list.append([r, c])

        for pac in pac_list:
            action2 = []
            state2 = []
            self.r = pac[0]
            self.c = pac[1]

            for stateX in state_list:
                # do not make while loop, will have bigger complexity
                if self.c - 1 >= 0:
                    if stateX.grid[self.r][self.c - 1] == " " or state.grid[self.r][self.c - 1] == "@":
                        miam = 1 if state.grid[self.r][self.c - 1] == "@" else 0
                        newState = State(self.grid_copy(stateX), stateX.foods - miam)
                        newState.grid[self.r][self.c - 1] = "$"
                        newState.grid[self.r][self.c] = " "
                        state2.append(newState)
                        action2.append("left")
                if self.c + 1 < state.nbc:
                    if state.grid[self.r][self.c + 1] == " " or state.grid[self.r][self.c + 1] == "@":
                        miam = 1 if state.grid[self.r][self.c + 1] == "@" else 0
                        newState = State(self.grid_copy(stateX), stateX.foods - miam)
                        newState.grid[self.r][self.c + 1] = "$"
                        newState.grid[self.r][self.c] = " "
                        state2.append(newState)
                        action2.append("right")
                if self.r - 1 >= 0:
                    if state.grid[self.r - 1][self.c] == " " or state.grid[self.r - 1][self.c] == "@":
                        miam = 1 if state.grid[self.r-1][self.c] == "@" else 0
                        newState = State(self.grid_copy(stateX), stateX.foods- miam)
                        newState.grid[self.r - 1][self.c] = "$"
                        newState.grid[self.r][self.c] = " "
                        state2.append(newState)
                        action2.append("top")
                if self.r + 1 < state.nbr:
                    if state.grid[self.r + 1][self.c] == " " or state.grid[self.r + 1][self.c] == "@":
                        miam = 1 if state.grid[self.r+1][self.c] == "@" else 0
                        newState = State(self.grid_copy(stateX), stateX.foods-miam)
                        newState.grid[self.r + 1][self.c] = "$"
                        newState.grid[self.r][self.c] = " "
                        state2.append(newState)
                        action2.append("down")
            action_list = action2
            state_list = state2

        for i in range(len(state_list)):
            yield (action_list[i], state_list[i])


    def goal_test(self, state):
        count = 0
        for r in range(state.nbr):
            for c in range(state.nbc):
                if state.grid[r][c] == '@':
                    count += 1
        return count == 0

    def grid_copy(self, state):
        grid2 = [[state.grid[i][j] for j in range(0, state.nbc)] for i in range(0, state.nbr)]
        return grid2


###############
# State class #
###############
class State:
    def __init__(self, grid, foods):
        self.nbr = len(grid)
        self.nbc = len(grid[0])
        self.grid = grid
        self.foods = foods

    def __str__(self):
        nsharp = self.nbc * 2 + 3
        s = "#" * nsharp
        s += '\n'
        for i in range(0, self.nbr):
            s += "# "
            for j in range(0, self.nbc):
                s += str(self.grid[i][j]) + " "
            s += "#"
            if i < self.nbr:
                s += '\n'
        s += "#" * nsharp
        return s

    def __eq__(self, other_state):
        for i in range(0, self.nbr):
            for j in range(0, self.nbc):
                if self.grid[i][j] != other_state.grid[i][j]: return False
        return True

    def __hash__(self):
        return hash(tuple([tuple(self.grid[i]) for i in range(0, len(self.grid))]))


######################
# Auxiliary function #
######################
def readInstanceFile(filename):
    lines = [[char for char in line.rstrip('\n')[1:][:-1]] for line in open(filename)]
    lines = lines[1:len(lines) - 1]
    n = len(lines)
    m = len(lines[0])
    grid_init = [[lines[i][j] for j in range(1, m, 2)] for i in range(0, n)]
    foods = 0
    for r in range(len(grid_init)):
        for c in range(len(grid_init[0])):
            if grid_init[r][c] == '@':
                foods += 1
    return grid_init, foods


######################
# Heuristic function #
######################
def heuristic(node):
    h = 0.0
    # ...
    # compute an heuristic value
    # ...
    return h


#####################
# Launch the search #
#####################
grid_init, foods = readInstanceFile(sys.argv[1])
init_state = State(grid_init, foods)

problem = Pacmen(init_state)

startTime = time.perf_counter()
node, nbExploredNodes = astar_graph_search(problem, heuristic)
endTime = time.perf_counter()

# example of print
path = node.path()
path.reverse()

print('Number of moves: ' + str(node.depth))
for n in path:
    print(n.state)  # assuming that the __str__ function of state outputs the correct format
    print()

#print("nb nodes explored = ",nb)
#print("time : " + str(endTime - startTime))