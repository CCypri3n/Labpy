import numpy as np
import pygame as game
from pygame.locals import *

class player():
    def __init__(self):
        self.maze = None
        self.position = None
        self.path = None
        self.win = None
        self.goal = None
        self.difficulty = 10
    
    def new_game(self, maze):
        self.maze = maze
        self.position = self.get_start()  # Starting position
        self.path = []  # Path taken by the player
        self.win = False
        self.goal = self.get_goal()
        self.difficulty += 1

    def get_start(self):
        # Find the starting position in the maze
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 10:
                    return {"x":x, "y":y}
        raise Exception(f"Start position not found in the maze {self.maze}")
    
    def get_goal(self):
        # Find the starting position in the maze
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 2:
                    return {"x":x, "y":y}
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
        
        x, y = self.position["x"], self.position["y"]
        
        try:
            if key == game.K_LEFT:
                if maze[self.position["y"]][self.position["x"]-1] != 1 and x > 0:
                    self.position["x"] -= 1
            if key == game.K_RIGHT:
                if maze[self.position["y"]][self.position["x"]+1] != 1 and x < len(self.maze[0])-1:
                    self.position["x"] += 1
            if key == game.K_UP:
                if maze[self.position["y"]-1][self.position["x"]] != 1 and y > 0:
                    self.position["y"] -= 1
            if key == game.K_DOWN:
                if maze[self.position["y"]+1][self.position["x"]] != 1 and y < len(self.maze[1]):
                    self.position["y"] += 1
        except Exception as e:
            print(e)

    def update(self, key):
        self.move(key) if not self.win else None # Update player position based on input
        self.win = True if self.position == self.goal else None
        return self.maze
    
    def followSol(self, solution: np.array):
        y, x = self.position["y"], self.position["x"]
        pass