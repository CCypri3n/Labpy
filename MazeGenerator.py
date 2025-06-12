import numpy as np

def createMaze(size=(10,10),start=(0,0), end=(10,10)):
    maze=np.zeros(size)
    maze[start[1]][start[0]] = 3
    maze[end[1]][end[0]] = 2
