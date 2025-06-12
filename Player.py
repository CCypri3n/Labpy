import numpy as np
import pygame as game
from pygame.locals import *

class player():
    def __init__(self, maze):
        self.maze = maze
        self.position = self.get_start()  # Starting position
        self.path = []  # Path taken by the player
    
    def get_start(self):
        # Find the starting position in the maze
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 3:
                    self.position = {"x":x, "y":y}
                    return self.position
        Exception("Start position not found in the maze")

    def move(self):
        # Implement movement logic based on direction
        keys = game.key.get_pressed()

        if keys[K_LEFT]:
            if self.maze[self.position["y"]][self.position["x"]-1] != 1:
                self.position["x"] -= 1
        if keys[K_RIGHT]:
            if self.maze[self.position["y"]][self.position["x"]+1] != 1:
                self.position["x"] += 1
        if keys[K_UP]:
            if self.maze[self.position["y"]-1][self.position["x"]] != 1:
                self.position["y"] -= 1
        if keys[K_DOWN]:
            if self.maze[self.position["y"]+1][self.position["x"]] != 1:
                self.position["y"] += 1

    def update(self):
        self.move()  # Update player position based on input

        return self.maze

