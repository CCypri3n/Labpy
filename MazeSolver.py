import numpy as np

def recursiveSolve(maze, start=(0,0)):
    #check if at arrival
    print(1)
    if maze[start[0]][start[1]]==2:
        return (True, maze)
    #draw path taken since not at arrival
    maze[start[0]][start[1]]=3
    ##UP
    #check if at top border
    if start[0] != 0:
        #save position above current as s
        s=(start[0]-1,start[1])
        #check if pos above current is free and unknown
        if maze[s[0]][s[1]] == 0 or maze[s[0]][s[1]] == 2:
            #recursive call to check for free path ahead
            isSolved, finalMaze = recursiveSolve(maze, s)
            #if winning path ahead return True
            if isSolved:
                return (True, finalMaze)
    #DOWN
    if start[0] != len(maze)-1:
        s=(start[0]+1,start[1])
        if maze[s[0]][s[1]] == 0 or maze[s[0]][s[1]] == 2:
            isSolved, finalMaze = recursiveSolve(maze, s)
            if isSolved:
                return (True, finalMaze)
    #LEFT
    if start[1] != 0:
        s=(start[0],start[1]-1)
        if maze[s[0]][s[1]] == 0 or maze[s[0]][s[1]] == 2:
            isSolved, finalMaze = recursiveSolve(maze, s)
            if isSolved:
                return (True, finalMaze)
    #RIGHT
    if start[1] != len(maze)-1:
        s=(start[0],start[1]+1)
        if maze[s[0]][s[1]] == 0 or maze[s[0]][s[1]] == 2:
            isSolved, finalMaze = recursiveSolve(maze, s)
            if isSolved:
                return (True, finalMaze)
    return (False, maze)

