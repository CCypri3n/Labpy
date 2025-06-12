import numpy as np
import pygame as game

import Display as Display
import Player as Player
import MazeSolver as MazeSol
import MazeGenerator as MazeGen

def main():
    # Initialize the display
    width, height = 600, 600
    win = Display.init_display(caption="Labpy", H=height, W=width)

    # Create a maze
    maze = np.array([[1, 3, 1, 2], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])#MazeGen.create_maze(20, 20)
    cell_size = min(width // len(maze[0]), height // len(maze))
    solutionTuple = MazeSol.recursiveSolve(maze, get_start(maze))
    P1 = False#Player.player(maze)

    clock = game.time.Clock()
    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
        if P1: maze = P1.update()  # Update player state
        win.fill((0, 0, 0))  # Fill the screen with black
        Display.display_maze(maze, cell_size) if not solutionTuple[0] else Display.display_solution(solutionTuple[1])
        if P1: Display.display_player(P1.position, cell_size)  # Draw the player on the maze
        game.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 FPS

    game.quit()

    # Solve the maze
    #solution = MazeSol.solve_maze(maze)

    # Display the maze and solution
    #Display.display_maze(maze)

def get_start(maze):
        # Find the starting position in the maze
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == 3:
                    position = (x, y)
                    return position
        Exception("Start position not found in the maze")

if __name__ == "__main__":
    main()