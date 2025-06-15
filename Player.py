import numpy as np
import pygame as game
from pygame.locals import *

class player():
    def __init__(self, diff):
        self.maze = None
        self.position = None
        self.path = []
        self.goal = None
        self.win = False
        self.difficulty = diff
    
    def next_level(self, maze):
        self.maze = maze
        self.position = self.get_start()  # Starting position
        self.goal = self.get_goal()
        if self.path: print("Path taken for this level: ", self.path)
        self.path = []  # Path taken by the player
        self.win = False

    def next_diff(self, inc: int):
        self.difficulty += inc
        return self.difficulty

    def get_start(self):
        # Find the starting position in the maze
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 10:
                    return (y, x)
        raise Exception(f"Start position not found in the maze {self.maze}")
    
    def get_goal(self):
        # Find the starting position in the maze
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 2:
                    return(y, x)
        raise Exception(f"End position not found in the maze {self.maze}")

    def move(self, key: game.event, maze: np.array = None):
        """This function changes the position of the player object based on keyboard input. If a maze is passed, that maze will be used instead of self.maze.

        Args:
            key (game.event): The pressed keys for movement
            maze (np.array, optional): A maze the player should move on. Defaults to None.
        """
        # Implement movement logic based on direction
        if type(maze) != np.array:
            maze = self.maze
        
        y, x = self.position
        try:
            if key == game.K_LEFT:
                if maze[y][x-1] != 1 and x > 0:
                    x -= 1
                    self.position = (y, x)
                    self.path.append(self.position)
            elif key == game.K_RIGHT:
                if maze[y][x+1] != 1 and x < len(self.maze[0])-1:
                    x += 1
                    self.position = (y, x)
                    self.path.append(self.position)
            elif key == game.K_UP:
                if maze[y-1][x] != 1 and y > 0:
                    y -= 1
                    self.position = (y, x)
                    self.path.append(self.position)
            elif key == game.K_DOWN:
                if maze[y+1][x] != 1 and y < len(self.maze[1]):
                    y += 1
                    self.position = (y, x)
                    self.path.append(self.position)
        except Exception as e:
            print(e)
            return

    def update(self, key):
        self.move(key) if not self.win else None # Update player position based on input
        self.win = True if self.position == self.goal else None
        return self.maze
    
    def followSol(self, solution: np.array):
        pass