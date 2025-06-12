import numpy as np
import random

def recursiveMazeGen(maze, start):
    maze[start["y"]][start["x"]] = 0  # Mark current cell as free space

    # Define directions: (dy, dx)
    directions = [
        {"y": -2, "x": 0},  # Up
        {"y": 2, "x": 0},   # Down
        {"y": 0, "x": -2},  # Left
        {"y": 0, "x": 2},   # Right
    ]
    random.shuffle(directions)  # Randomize directions for more interesting mazes

    for d in directions:
        ny = start["y"] + d["y"]
        nx = start["x"] + d["x"]
        # Check if neighbor is within bounds
        if 0 <= ny < maze.shape[0] and 0 <= nx < maze.shape[1]:
            if maze[ny][nx] == 1:  # If neighbor cell is still a wall
                # Carve passage between current and neighbor
                maze[start["y"] + d["y"] // 2][start["x"] + d["x"] // 2] = 0
                # Recursively continue from neighbor
                recursiveMazeGen(maze, {"y": ny, "x": nx})

def genMaze(size, start):
    maze = np.ones((size, size), dtype=int)
    recursiveMazeGen(maze, start)
    # Optionally, set entrance and exit
    maze[1][0] = 0  # Entrance
    maze[size-2][size-1] = 0  # Exit

    print(maze)



