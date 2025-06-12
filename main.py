import numpy as np
import pygame as game

import Display as display
import MazeSolver as MazeSol
import MazeGenerator as MazeGen

def main():
    # Initialize the display
    win = display.init_display(Caption="Labpy", H=600, W=600)

    # Create a maze
    maze = np.array([[1, 3, 1, 2], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])#MazeGen.create_maze(20, 20)
    Player = player(maze)

    clock = game.time.Clock()
    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False

        win.fill((0, 0, 0))  # Fill the screen with black
        display.display_maze(maze)
        game.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 FPS

    game.quit()

    # Solve the maze
    #solution = MazeSol.solve_maze(maze)

    # Display the maze and solution
    #display.display_maze(maze)

if __name__ == "__main__":
    main()

class player():
    def __init__(self, maze):
        self.maze = maze
        self.position = (0, 0)  # Starting position
        self.path = []  # Path taken by the player

    def move(self, direction):
        # Implement movement logic based on direction
        pass

    def draw(self):
        # Implement drawing logic for the player
        pass