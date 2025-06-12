import numpy as np
import pygame as game

import Display as display
import MazeSolver as MazeSolver

def main():
    # Initialize the display
    WIN = display.init_display()

    # Create a maze
    maze = MazeSolver.create_maze(20, 20)

    clock = game.time.Clock()
    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False

        WIN.fill((0, 0, 0))  # Fill the screen with black
        
        game.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 FPS

    game.quit()

    # Solve the maze
    #solution = MazeSolver.solve_maze(maze)

    # Display the maze and solution
    #display.display_maze(maze)

if __name__ == "__main__":
    main()