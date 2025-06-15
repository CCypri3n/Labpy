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
    [1, 2, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])
    
def new_game(win: game.display, width: int, height: int):
    # Create a maze
    startdifficulty = 9
    P1 = Player.player(startdifficulty)
    
    next_level(win, width, height, P1)

    game.quit()
    exit()

def next_level(win: game.display, width: int, height: int, P1: Player.player):
    size = P1.difficulty+1 ## Add +1 to old difficulty, in order to generate correct maze.
    while True:
        try:
            maze = MazeGen.genMaze(size, (random.choice(range(0, size-1)), random.choice(range(0, size-1))))
            get_start(maze)
            get_goal(maze)
            break
        except:
            continue
    P1.next_level(maze) ## Update difficulty, reset variables and update maze and positions.
    cell_size = min(width // len(maze[0]), height // len(maze))

    ## Set Variables
    Display.display_maze.count = 0.0 ## Iteration count
    Display.display_solution.animationInt = 10 ## Current solution path (Starts at ten, then increases)
    Display.display_solution.count = 0.0 ## Iteration count
    Display.display_win.animationInt = 0 ## Animation frame
    Display.display_win.count = 0.0 ## Iteration count

    play_loop(win, maze, cell_size, P1 if P1 else None)

def play_loop(win: game.display, maze: np.array, cell_size: int, P1: Player.player = None):
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
                    solve_loop(win, maze, cell_size, P1 if P1 else None)
                    break
                else:
                    if P1: maze = P1.update(event.key)
        updateRect = Display.display_maze(maze, cell_size)
        if P1 and len(maze)-1 <= Display.display_maze.count: updateRect = Display.display_player(P1, cell_size)  # Draw the player on the maze
        game.display.update(updateRect)  # Update the display
        clock.tick(fps)
        if P1.win:
            running = False

    win_loop(win, maze, cell_size, P1)

def solve_loop(win: game.display, maze: np.array, cell_size, P1: Player.player = None):
    solutionTuple = (0, 0)
    solutionTuple = MazeSol.solveMaze(maze, get_start(maze))
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
                    play_loop(win, maze, cell_size, P1 if P1 else None)
                    break
        updateRect = Display.display_solution(solutionTuple[1], cell_size)
        if P1: Display.display_player(P1, cell_size)  # Draw the player on the maze
        game.display.update(updateRect if updateRect else game.Rect(0, 0, width, height))  # Update the display
        clock.tick(fps)

def win_loop(win: game.display, maze: np.array, cell_size: int, P1: Player.player):
    running = True
    oldRect = None
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
                game.quit()
                exit()
        updateRect, running = Display.display_win(maze, cell_size)
        Display.display_player(P1, cell_size)  # Draw the player on the maze
        game.display.update(updateRect)  # Update the display
        clock.tick(fps)
    win.fill((0, 0, 0))
    game.display.flip()
    next_level(win, width, height, P1)

def get_start(maze):
    # Find the starting position in the maze
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 10:
                position = (y, x)
                return position
    Exception("Start position not found in the maze: {maze}")

def get_goal(maze):
        # Find the starting position in the maze
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == 2:
                    return (y, x)
        Exception("End position not found in the maze: {maze}")

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(5000)
    fps = 60
    clock = game.time.Clock()
    width, height = 700, 700
    win = Display.init_display(caption="Labpy", H=height, W=width)
    new_game(win, width, height)