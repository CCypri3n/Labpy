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

def new_game(win: game.display, width: int, height: int, P1: Player.player):
    # Create a maze
    
    size = P1.difficulty
    while True:
        try:
            maze = MazeGen.genMaze(size, (random.choice(range(0, size-1)), random.choice(range(0, size-1))))
            get_start(maze)
            get_goal(maze)
            break
        except:
            continue

    cell_size = min(width // len(maze[0]), height // len(maze))
    P1.new_game(maze)

    play_loop(win, maze, cell_size, P1 if P1 else None)

    game.quit()
    exit()

def play_loop(win: game.display, maze: np.array, cell_size: int, P1: Player.player = None):
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
                    animationInt = solve_loop(win, maze, cell_size, P1 if P1 else None)
                    break
                else:
                    if P1: maze = P1.update(event.key)
        win.fill((0, 0, 0))  # Fill the screen with black
        Display.display_maze(maze, cell_size) if not P1.win else bool(running)
        if P1: Display.display_player(P1.position, cell_size)  # Draw the player on the maze
        game.display.flip()  # Update the display
        clock.tick(fps)
        if P1.win:
            running = False
    win_loop(win, maze, cell_size, P1)

def solve_loop(win: game.display, maze: np.array, cell_size, P1: Player.player = None):
    solutionTuple = (0, 0)
    solutionTuple = MazeSol.solveMaze(maze, get_start(maze))
    running = True
    animationInt = 10
    iterCount = 0
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
                game.quit()
                exit()
            elif event.type == game.KEYDOWN:
                if event.key == game.K_SPACE and animationInt >= np.max(solutionTuple[1]):
                    running = False
                    play_loop(win, maze, cell_size, P1 if P1 else None)
                    break
        win.fill((0, 0, 0))  # Fill the screen with black
        iterCount += 1
        if iterCount == 2:
            animationInt += 1
        iterCount %= 2
        Display.display_solution(solutionTuple[1], cell_size, animationInt)
        if P1: Display.display_player(P1.position, cell_size)  # Draw the player on the maze
        game.display.flip()  # Update the display
        clock.tick(fps)

def win_loop(win: game.display, maze: np.array, cell_size: int, P1: Player.player):
    i = 0
    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
                game.quit()
                exit()
        i += 1
        running = False if i >= 60 else True
        win.fill((0, 0, 0))  # Fill the screen with black
        Display.display_win(maze, cell_size)
        Display.display_player(P1.position, cell_size)  # Draw the player on the maze
        game.display.flip()  # Update the display
        clock.tick(fps)
    new_game(win, width, height, P1)

def get_start(maze):
    # Find the starting position in the maze
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == 10:
                position = (y, x)
                return position
    Exception("Start position not found in the maze {maze}")

def get_goal(maze):
        # Find the starting position in the maze
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == 2:
                    return {"x":x, "y":y}
        raise Exception("End position not found in the maze {maze}")

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(5000)
    fps = 60
    clock = game.time.Clock()
    width, height = 700, 700
    win = Display.init_display(caption="Labpy", H=height, W=width)
    P1 = Player.player()
    new_game(win, width, height, P1)