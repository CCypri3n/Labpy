import numpy as np

testmaze = np.array([
    [1, 3, 1, 1, 1, 1, 1, 1, 1, 1],
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
def cleanGrid(inGrid):
    outGrid = inGrid.copy()
    for y in inGrid:
        for x, val in enumerate(y):
            if val not in [0, 1, 2, 10]:
                outGrid[y][x] = 0


def getEndPos(maze) -> tuple:
    for y in maze:
        for x, val in enumerate(y):
            if val == 2:
                return (y, x)
    return None


def getFreeNeighbours(pos, grid):
    # UP
    if pos[0] != 0:
        if grid[pos[0] - 1][pos[1]] in [0, 2]:
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
    current = [start]
    solved = False
    iterCount = 0
    grid = inMaze.copy()
    while not solved:
        iterCount += 1
        print(iterCount)
        future = []
        for curPoint in current:
            print(current)
            if grid[curPoint[0]][curPoint[1]] == 2:
                solved = True
            else:
                grid[curPoint[0]][curPoint[1]] = 10 + iterCount
            future += [neighbour for neighbour in getFreeNeighbours(curPoint, grid)]
        current = future.copy()
        if current == []:
            break
    return (solved, grid)


def quickestPath(breadthSearchedMaze):
    grid_with_path = cleanGrid(breadthSearchedMaze.copy())
    end = getEndPos(breadthSearchedMaze)
    if end == None:
        raise ValueError("No end point found")
    else:
        pos = end

        while breadthSearchedMaze[pos[0]][pos[1]] != 10:
            curVal = breadthSearchedMaze[pos[0]][pos[1]]
            # UP
            if pos[0] != 0:
                if breadthSearchedMaze[pos[0] - 1][pos[1]] == curVal - 1:
                    grid_with_path[pos[0] - 1][pos[1]] = 3
            # Down
            elif pos[0] != len(breadthSearchedMaze) - 1:
                if breadthSearchedMaze[pos[0] + 1][pos[1]] == curVal - 1:
                    grid_with_path[pos[0] + 1][pos[1]] = 3
            # Left
            elif pos[1] != 0:
                if breadthSearchedMaze[pos[0]][pos[1] - 1] == curVal - 1:
                    grid_with_path[pos[0]][pos[1] - 1] = 3
            # RIGHT
            elif pos[1] != len(breadthSearchedMaze) - 1:
                if breadthSearchedMaze[pos[0]][pos[1] + 1] == curVal - 1:
                    grid_with_path[pos[0]][pos[1] + 1] = 3
        return grid_with_path


def solveMaze(inMaze, start=(0, 0)):
    return quickestPath(breadthFirstSolve(inMaze, start))


#print(solveMaze(testmaze, start=(0, 1)))


