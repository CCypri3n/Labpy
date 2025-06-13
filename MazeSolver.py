import numpy as np

testmaze = np.array([
    [1, 10, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 2, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])


# Helperfuncs
#reverts breadthsearched maze to original
def cleanGrid(inGrid):
    #copy to not modify the original
    outGrid = inGrid.copy()
    #iterate over every cell
    for y, row in enumerate(inGrid):
        for x, val in enumerate(row):
            #check if value is clutter, if so set to 0
            if val not in [0, 1, 2, 10]:
                outGrid[y][x] = 0
    return outGrid

#finds pos of maze arrival
def getEndPos(maze) -> tuple:
    #iterate over every cell
    for y, row in enumerate(maze):
        for x, val in enumerate(row):
            #if is endcell return pos
            if val == 2:
                return (y, x)
    #else return None
    return None

#finds unvisited accessible neighbours
def getFreeNeighbours(pos, grid):
    # UP
    #check for top border
    if pos[0] != 0:
        #check for value of cell above
        if grid[pos[0] - 1][pos[1]] in [0, 2]:
            #yield said value
            yield (pos[0] - 1, pos[1])
    # Down
    if pos[0] != len(grid) - 1:
        if grid[pos[0] + 1][pos[1]] in [0, 2]:
            yield (pos[0] + 1, pos[1])
    # Left
    if pos[1] != 0:
        if grid[pos[0]][pos[1] - 1] in [0, 2]:
            yield (pos[0], pos[1] - 1)
    # RIGHT
    if pos[1] != len(grid) - 1:
        if grid[pos[0]][pos[1] + 1] in [0, 2]:
            yield (pos[0], pos[1] + 1)


# Actual solving funcs
def depthFirstSolve(inMaze, start=(0, 0)):
    # check if at arrival
    maze = inMaze.copy()
    if maze[start[0]][start[1]] == 2:
        return (True, maze)
    # draw path taken since not at arrival
    maze[start[0]][start[1]] = 4
    ##UP
    # check if at top border
    if start[0] != 0:
        # save position above current as s
        s = {"y": start[0] - 1, "x": start[1]}
        # check if pos above current is free and unknown
        if maze[s[0]][s[1]] == 0 or maze[s[0]][s[1]] == 2:
            # recursive call to check for free path ahead
            isSolved, finalMaze = depthFirstSolve(maze, s)
            # if winning path ahead return True
            if isSolved:
                return (True, finalMaze)
    # DOWN
    if start[0] != len(maze) - 1:
        s = (start[0] + 1, start[1])
        if maze[s[0]][s[1]] == 0 or maze[s[0]][s[1]] == 2:
            isSolved, finalMaze = depthFirstSolve(maze, s)
            if isSolved:
                return (True, finalMaze)
    # LEFT
    if start[1] != 0:
        s = (start[0], start[1] - 1)
        if maze[s[0]][s[1]] == 0 or maze[s[0]][s[1]] == 2:
            isSolved, finalMaze = depthFirstSolve(maze, s)
            if isSolved:
                return (True, finalMaze)
    # RIGHT
    if start[1] != len(maze) - 1:
        s = (start[0], start[1] + 1)
        if maze[s[0]][s[1]] == 0 or maze[s[0]][s[1]] == 2:
            isSolved, finalMaze = depthFirstSolve(maze, s)
            if isSolved:
                return (True, finalMaze)

    return (False, maze)


def breadthFirstSolve(inMaze, start=(0, 0)):
    #list of cells we are currently interested in
    current = [start]
    solved = False
    #counts iterations
    iterCount = 0
    #copy to avoid modifying the original
    grid = inMaze.copy()
    while not solved:
        #keeps count
        iterCount += 1
        #temporary storage which is emptied at every iteration
        future = []
        #iterate over current points
        for curPoint in current:
            #check if arrival
            if grid[curPoint[0]][curPoint[1]] == 2:
                solved = True
            #if not, paint
            else:
                grid[curPoint[0]][curPoint[1]] = 10 + iterCount
            #add all neighbours of just painted cells to temp list
            future += [neighbour for neighbour in getFreeNeighbours(curPoint, grid)]
        #after finishing iterations, define content of temp list as current for next iter
        current = future.copy()
        #check if there are no cells left to check
        if current == []:
            break
    #return if solved, the solved grid and the number of iterations
    return (solved, grid, iterCount)

#finds the quickest path going from a breathsearchedmaze and the pathlength
def quickestPath(breadthSearchedMaze, pathlen):
    #copy grid to avoid modifying the original
    grid_with_path = cleanGrid(breadthSearchedMaze.copy())
    #finds end position
    end = getEndPos(breadthSearchedMaze)
    #check if maze has end point
    if end == None:
        raise ValueError("No end point found")
    else:
        #define starting pos as end
        pos = end
        #redefine value of end for algorithm to work
        breadthSearchedMaze[end[0]][end[1]]=pathlen+10
        #iterate as long as beginning not reached
        while breadthSearchedMaze[pos[0]][pos[1]] != 11:
            #save current value
            curVal = breadthSearchedMaze[pos[0]][pos[1]]
            foundNextStep=False
            # UP
            #check for top border
            if pos[0] != 0 and not foundNextStep:
                #check if value is next lowest
                if breadthSearchedMaze[pos[0] - 1][pos[1]] == curVal - 1:
                    #if so paint with 3
                    grid_with_path[pos[0] - 1][pos[1]] = 3
                    pos=(pos[0] - 1, pos[1])
                    foundNextStep = True
            # Down
            if pos[0] != len(breadthSearchedMaze) - 1 and not foundNextStep:
                if breadthSearchedMaze[pos[0] + 1][pos[1]] == curVal - 1:
                    grid_with_path[pos[0] + 1][pos[1]] = 3
                    pos = (pos[0] + 1, pos[1])
                    foundNextStep = True
            # Left
            if pos[1] != 0 and not foundNextStep:
                if breadthSearchedMaze[pos[0]][pos[1] - 1] == curVal - 1:
                    grid_with_path[pos[0]][pos[1] - 1] = 3
                    pos = (pos[0], pos[1] - 1)
                    foundNextStep = True
            # RIGHT
            if pos[1] != len(breadthSearchedMaze) - 1 and not foundNextStep:
                if breadthSearchedMaze[pos[0]][pos[1] + 1] == curVal - 1:
                    grid_with_path[pos[0]][pos[1] + 1] = 3
                    foundNextStep = True
                    pos = (pos[0], pos[1] + 1)
        return grid_with_path


def solveMaze(inMaze, start=(0, 0)):
    solved, prepedMaze, pathlen = breadthFirstSolve(inMaze, start)
    if solved:
        return quickestPath(prepedMaze, pathlen)
    else:
        return None


print(solveMaze(testmaze, start=(0, 1)))


