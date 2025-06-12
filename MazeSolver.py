import numpy as np

def depthFirstSolve(inMaze, start={"x":0, "y":0}):
    #check if at arrival
    maze=inMaze.copy()
    if maze[start["y"]][start["x"]]==2:
        return (True, maze)
    #draw path taken since not at arrival
    maze[start["y"]][start["x"]]=3
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

