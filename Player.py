import numpy as np
import pygame as game

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
                    self.position = (x, y)
                    return self.position
        Exception("Start position not found in the maze")

    def move(self):
        # Implement movement logic based on direction
        keys = game.key.get_pressed()

        if keys[K_LEFT]:
            self.position[0] -= 1
        if keys[K_RIGHT]:
            self.position[0] += 1
        if keys[K_UP]:
            self.position[1] -= 1
        if keys[K_DOWN]:
            self.position[1] += 1

    def update(self):
        self.move()  # Update player position based on input

        return self.maze

