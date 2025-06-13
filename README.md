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