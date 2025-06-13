import numpy as np

def depthFirstSolve(inMaze, start={"x":0, "y":0}):
    #check if at arrival
    maze=inMaze.copy()
    if maze[start["y"]][start["x"]]==2:
        return (True, maze)
    #draw path taken since not at arrival
    maze[start["y"]][start["x"]]=4
    ##UP
    #check if at top border
    if start["y"] != 0:
        #save position above current as s
        s={"y":start["y"]-1,"x":start["x"]}
        #check if pos above current is free and unknown
        if maze[s["y"]][s["x"]] == 0 or maze[s["y"]][s["x"]] == 2:
            #recursive call to check for free path ahead
            isSolved, finalMaze = depthFirstSolve(maze, s)
            #if winning path ahead return True
            if isSolved:
                return (True, finalMaze)
    #DOWN
    if start["y"] != len(maze)-1:
        s={"y": start["y"]+1,"x":start["x"]}
        if maze[s["y"]][s["x"]] == 0 or maze[s["y"]][s["x"]] == 2:
            isSolved, finalMaze = depthFirstSolve(maze, s)
            if isSolved:
                return (True, finalMaze)
    #LEFT
    if start["x"] != 0:
        s={"y": start["y"],"x": start["x"]-1}
        if maze[s["y"]][s["x"]] == 0 or maze[s["y"]][s["x"]] == 2:
            isSolved, finalMaze = depthFirstSolve(maze, s)
            if isSolved:
                return (True, finalMaze)
    #RIGHT
    if start["x"] != len(maze)-1:
        s={"y": start["y"],"x": start["x"]+1}
        if maze[s["y"]][s["x"]] == 0 or maze[s["y"]][s["x"]] == 2:
            isSolved, finalMaze = depthFirstSolve(maze, s)
            if isSolved:
                return (True, finalMaze)

    return (False, maze)

def breadthFirstSolve(inMaze, start = (0,0)):
    current=[start]
    solved= False
    iterCount=0
    grid=inMaze.copy()
    while not solved:
        iterCount+=1
        for curPoint in current:
            if grid[curPoint[0]][curPoint[1]]==2:
                solved=True
            else:
                grid[curPoint[0]][curPoint[1]]=10+iterCount
            current.append([neighbour for neighbour in getFreeNeighbours(curPoint, grid)])
            current.remove(curPoint)
        if current == []:
            break
    return (solved, grid)



def getFreeNeighbours(pos, grid):
    #UP
    if pos[0] != 0:
        if grid[pos[0]-1][pos[1]] in [0,2] :
            yield (pos[0]-1,pos[1])
    # Down
    if pos[0] != len(grid)-1:
        if grid[pos[0] + 1][pos[1]] in [0,2]:
            yield (pos[0] - 1, pos[1])
    # Left
    if pos[1] != 0:
        if grid[pos[0]][pos[1] - 1 ] in [0,2]:
            yield (pos[0], pos[1] - 1)
    # RIGHT
    if pos[1] != len(grid)-1:
        if grid[pos[0]][pos[1]+1] in [0,2]:
            yield (pos[0],pos[1]+1)




