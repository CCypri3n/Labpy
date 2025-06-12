import numpy as np
import random as r
import MazeSolver as ms

def createMaze(size=(10,10),start=(0,0), end=(10,10)):
    maze=np.zeros(size)
    maze[start[0]][start[1]] = 3
    maze[end[0]][end[1]] = 2


