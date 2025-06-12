import numpy as np
import pygame as game
from pygame.locals import *

class player():
    def __init__(self, maze):
        self.maze = maze
        self.position = self.get_start()  # Starting position
        self.path = []  # Path taken by the player
        self.win = False
        self.goal = self.get_goal()
    
    def get_start(self):
        # Find the starting position in the maze
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 3:
                    self.position = {"x":x, "y":y}
                    return self.position
        Exception("Start position not found in the maze")
    
    def get_goal(self):
        # Find the starting position in the maze
        for y, row in enumerate(self.maze):
            for x, cell in enumerate(row):
                if cell == 2:
                    self.goal = {"x":x, "y":y}
                    return self.goal
        Exception("Start position not found in the maze")

    def move(self):
        # Implement movement logic based on direction
        keys = game.key.get_pressed()
        
        try:
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
        except Exception as e:
            print(e)

    def update(self):
        self.move()  # Update player position based on input
        if self.position == self.goal:
            self.win = True

        return self.maze

