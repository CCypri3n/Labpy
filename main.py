import numpy as np
import pygame as game
import random

import Display as Display
import Player as Player
import MazeSolver as MazeSol
import MazeGenerator as MazeGen

maze10 = np.array([
    [1, 10, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

def main(win: game.display, width: int, height: int, size: int = None, start: tuple = (0, 0)):
    # Create a maze
    maze = MazeGen.genMaze(size, start) if size else maze10
    cell_size = min(width // len(maze[0]), height // len(maze))
    print(maze, cell_size)

    ## Set Variables
    Display.display_maze.count = 0.0
    Display.display_solution.animationInt = 10
    Display.display_solution.count = 0
    
    win.fill((0, 0, 0))
    game.display.flip()

    play_loop(win, maze, cell_size)

    game.quit()
    exit()

def play_loop(win: game.display, maze: np.array, cell_size: int):
    global animationInt
    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
                game.quit()
                exit()
            elif event.type == game.KEYDOWN:
                if event.key == game.K_SPACE:
                    running = False
                    animationInt = solve_loop(win, maze, cell_size)
                    break
        win.fill((0, 0, 0))  # Fill the screen with black
        Display.display_maze(maze, cell_size)
        game.display.flip()  # Update the display
        clock.tick(fps)

def solve_loop(win: game.display, maze: np.array, cell_size):
    solutionTuple = (0, 0)
    solutionTuple = MazeSol.solveMaze(maze, get_start(maze))
    running = True
    Display.display_solution.animationInt = 10
    Display.display_solution.count = 0
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
                game.quit()
                exit()
            elif event.type == game.KEYDOWN:
                if event.key == game.K_SPACE:
                    running = False
                    all_way_solve_loop(win, maze, cell_size)
                    break
        Display.display_solution(solutionTuple[1], cell_size)
        game.display.flip()  # Update the display
        clock.tick(fps)

def all_way_solve_loop(win: game.display, maze: np.array, cell_size):
    solutionTuple = (0, 0)
    solutionTuple = MazeSol.breadthFirstSolve(maze, get_start(maze))
    running = True
    animationInt = 10
    Display.display_solution.animationInt = 10
    Display.display_solution.count = 0
    Display.display_maze(maze, cell_size)
    game.display.flip()
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
                game.quit()
                exit()
            elif event.type == game.KEYDOWN:
                if event.key == game.K_SPACE:
                    running = False
                    play_loop(win, maze, cell_size)
                    break
        updateRects = Display.display_solution(solutionTuple[1], cell_size)
        game.display.update(updateRects)  # Update the display
        clock.tick(fps)

def get_start(maze):
    # Find the starting position in the maze
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 10:
                position = (y, x)
                return position
    Exception("Start position not found in the maze")

if __name__ == "__main__":
    print("\n\n------------ Labpy V1 ------------\nmade with ♥ by CCypri3n and Ruby\n\nUse:\n - Enter a maze size (between 2 and 100) for random maze generation or press enter to select the default maze.\n - Press space to see the path, press space again to see the algorithm.")

    size, start = None, None
    size = input("\nPlease enter a labyrinth size (Leave blank for default size 10 maze): ")
    while not size.isdigit() and size:
        size = input("\nPlease enter a labyrinth size: ")
    print("\n\n\n Loading ... \n\n\n")
    if size.isdigit():
        size = int(size)
        start = (random.choice(range(0, size)), random.choice(range(0, size)))

    import sys
    sys.setrecursionlimit(10000)
    fps = 60
    clock = game.time.Clock()
    width, height = 700, 700
    win = Display.init_display(caption="Labpy", H=height, W=width)

    main(win, width, height, size if size else None, start if start else None)