import numpy as np
import pygame as game

import Display as Display
import Player as Player
import MazeSolver as MazeSol
import MazeGenerator as MazeGen

maze10 = np.array([
    [1, 3, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 2, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

def main():
    # Initialize the display
    width, height = 700, 700
    win = Display.init_display(caption="Labpy", H=height, W=width)

    # Create a maze
    maze = MazeGen.genMaze(100, {"x": 0, "y": 25})
    cell_size = min(width // len(maze[0]), height // len(maze))
    P1 = Player.player(maze)

    main_loop(win, maze, cell_size, P1 if P1 else None)

    game.quit()

def main_loop(win: game.display, maze: np.array, cell_size: int, P1: Player.player = None):
    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
                game.quit()
            elif event.type == game.KEYDOWN:
                if event.key == game.K_SPACE:
                    running = False
                    solve_loop(win, maze, cell_size, P1 if P1 else None)
                    break
        if P1: maze = P1.update()  # Update player state
        win.fill((0, 0, 0))  # Fill the screen with black
        Display.display_maze(maze, cell_size)
        if P1: Display.display_player(P1.position, cell_size)  # Draw the player on the maze
        game.display.flip()  # Update the display
        clock.tick(fps)

def solve_loop(win: game.display, maze: np.array, cell_size, P1: Player.player = None):
    solutionTuple = (0, 0)
    solutionTuple = MazeSol.breadthFirstSolve(maze, get_start(maze))
    print(solutionTuple)
    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
                game.quit()
            elif event.type == game.KEYDOWN:
                if event.key == game.K_SPACE:
                    running = False
                    main_loop(win, maze, cell_size, P1 if P1 else None)
                    break
        win.fill((0, 0, 0))  # Fill the screen with black
        Display.display_solution(solutionTuple[1], cell_size)
        if P1: Display.display_player(P1.position, cell_size)  # Draw the player on the maze
        game.display.flip()  # Update the display
        clock.tick(fps)

def get_start(maze):
        # Find the starting position in the maze
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == 10:
                    position = {"x":x, "y":y}
                    return position
        Exception("Start position not found in the maze")

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(5000)
    fps = 25
    clock = game.time.Clock()
    main()