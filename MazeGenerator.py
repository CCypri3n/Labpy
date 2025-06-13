import numpy as np
import random

def recursiveMazeGen(maze, start):
    maze[start[0]][start[1]] = 0  # Mark current cell as free space

    # Define directions: (dy, dx)
    directions = [
        (-2,0),  # Up
        (2,0),   # Down
        (0,-2),  # Left
        (0,2),   # Right
    ]
    random.shuffle(directions)  # Randomize directions for more interesting mazes

    for d in directions:
        ny = start[0] + d[0]
        nx = start[1] + d[1]
        # Check if neighbor is within bounds
        if 0 <= ny < maze.shape[0] and 0 <= nx < maze.shape[1]:
            if maze[ny][nx] == 1:  # If neighbor cell is still a wall
                # Carve passage between current and neighbor
                maze[start[0] + d[0] // 2][start[1] + d[1] // 2] = 0
                # Recursively continue from neighbor
                recursiveMazeGen(maze, (ny, nx))
    return maze

def genMaze(size, start):
    maze = np.ones((size, size), dtype=int)
    maze = recursiveMazeGen(maze, start)
    # Optionally, set entrance and exit
    maze[1][0] = 0  # Entrance
    maze[size-2][size-1] = 0  # Exit
    maze[start[0]][start[1]]=10
    end = (random.randint(0, size), random.randint(0, size))
    maze[end[1]][end[0]]=2
    return maze


if __name__ == "__main__":
    print(genMaze(20,(0,0)))
