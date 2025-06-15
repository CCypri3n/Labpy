import numpy as np
import pygame as game
import random

import DisplayGame as Display
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

# class maze:
# class game:

def new_game(win: Display.window):
    # Create a maze
    startdifficulty = 9
    P1 = Player.player(startdifficulty)
    
    next_level(win, P1)

    game.quit()
    exit()

def next_level(win: Display.window, P1: Player.player):
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
    win.cell_size = min(win.board_size[1] // len(maze[0]), win.board_size[0] // len(maze))

    ## Set Variables
    Display.display_maze.count = 0.0 ## Iteration count
    Display.display_solution.animationInt = 10 ## Current solution path (Starts at ten, then increases)
    Display.display_solution.count = 0.0 ## Iteration count
    Display.display_win.animationInt = 0 ## Animation frame
    Display.display_win.count = 0.0 ## Iteration count

    play_loop(win, maze, P1 if P1 else None)

def play_loop(win: Display.window, maze: np.array, P1: Player.player):
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
                    solve_loop(win, maze, P1 if P1 else None)
                    break
                else:
                    if P1: maze = P1.update(event.key)
        updateRect = Display.display_maze(win, maze)
        if P1 and len(maze) < Display.display_maze.count: updateRect = Display.display_player(win, P1)  # Draw the player on the maze
        win.update(updateRect)  # Update the display
        clock.tick(fps)
        if P1.win:
            running = False

    win_loop(win, maze, P1)

def solve_loop(win: Display.window, maze: np.array, P1: Player.player):
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
                    play_loop(win, maze, P1 if P1 else None)
                    break
        updateRect = Display.display_solution(win, solutionTuple[1])
        if P1: Display.display_player(win, P1)  # Draw the player on the maze
        win.update(updateRect if updateRect else None)  # Update the display
        clock.tick(fps)

def win_loop(win: Display.window, maze: np.array, P1: Player.player):
    running = True
    oldRect = None
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
                game.quit()
                exit()
        updateRect, running = Display.display_win(win, maze)
        Display.display_player(win, P1)  # Draw the player on the maze
        win.update(updateRect)  # Update the display
        clock.tick(fps)
    win.fill((0, 0, 0), win.board)
    game.display.flip()
    next_level(win, P1)

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
    board = 700
    side_menu = 30
    win = Display.init_display(caption="Labpy", H=board, side=side_menu)
    new_game(win)