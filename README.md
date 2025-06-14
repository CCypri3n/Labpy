# Labpy

A simple python project, to solve and display mazes.

## Maze formats

Mazes are represented as 2D-Numpy-Arrays containing integers:
0 : no wall
1 : wall
2 : endpoint of the maze
10 : starting tile
4 : unordered solution path
11+ : the breadth-first search layers

## Coordinates

Coordinates are generally to be passed on as tuples in the (y,x) format.

## TODO - Cyprien

- Change velocity of Player depending on length of keyhold
- move player with keyhold
- "Run from breadthfirstSolve" gamemode

## Errors

- MazeGeneration without starting position: Exception: Start position not found in the maze
    [[2 0 0]
    [0 1 0]
    [0 0 0]]
- '''Traceback (most recent call last):
  File "/Users/cyprien/Coding/Gits/Labpy/main.py", line 139, in <module>
    main(win, width, height, size if size else None, start if start else None)
  File "/Users/cyprien/Coding/Gits/Labpy/main.py", line 25, in main
    maze = MazeGen.genMaze(size, start) if size else maze10
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/cyprien/Coding/Gits/Labpy/MazeGenerator.py", line 36, in genMaze
    maze[end[1]][end[0]]=2 ~~~~~~~~~~~~^^^^^^^^
  IndexError: index 100 is out of bounds for axis 0 with size 100 '''
- No solution shown (solveMaze): index 19 is out of bounds for axis 0 with size 19
