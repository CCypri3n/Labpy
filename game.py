import numpy as np
import pygame as game
import random

import DisplayGame as Display
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

class maze:
    def __init__(self):
        self.mazearray = None
        self.cell_size = None
        self.size = None

    
    def new_maze(self):
        while True:
            try:
                self.mazearray = MazeGen.genMaze(self.size, (random.choice(range(0, self.size-1)), random.choice(range(0, self.size-1))))
                self.get_start(self.mazearray)
                self.get_end(self.mazearray)
                return
            except:
                continue
    
    def get_start(self, maze: np.array = None):
        # Find the starting position in the maze
        for y, row in enumerate(self.mazearray):
            for x, cell in enumerate(row):
                if cell == 10:
                    position = (y, x)
                    return position
        Exception(f"Start position not found in the maze: {self.mazearray}")

    def get_end(self, maze: np.array = None):
        # Find the starting position in the maze
        for y, row in enumerate(self.mazearray):
            for x, cell in enumerate(row):
                if cell == 2:
                    position = (y, x)
                    return position
        Exception(f"Start position not found in the maze: {self.mazearray}")



class mainFrame:
    def __init__(self):
        self.fps = 60
        self.clock = game.time.Clock()
        self.board = 700
        self.side_menu = 50
        self.win = Display.init_display(caption="Labpy", H=self.board, side=self.side_menu)
        self.P1 = Player.player(8)
        self.maze = maze()
        self.loop = "init"

        Display.display_maze.count = 0.0 ## Iteration count
        Display.display_solution.animationInt = 10 ## Current solution path (Starts at ten, then increases)
        Display.display_solution.count = 0.0 ## Iteration count
        Display.display_win.animationInt = 0 ## Animation frame
        Display.display_win.count = 0.0 ## Iteration count
    
    def main(self):
        updateRect = None
        while True:
            if self.loop == "solve":
                updateRect = self.solve_loop()
            elif self.loop == "win":
                updateRect = self.win_loop() 
            elif self.loop == "play":
                updateRect = self.play_loop()
            elif self.loop == "menu":
                updateRect = self.menu_loop()   
            elif self.loop == "next_level":
                self.next_level()
            self.clock.tick(self.fps)
            self.win.update(updateRect if updateRect else None)
    
    
    def menu_loop(self):
        pass

    def next_level(self):
        Display.init_level(self.win, self.P1)
        self.maze.size = self.P1.next_diff(2)
        self.maze.new_maze()
        self.P1.next_level(self.maze.mazearray) ## Update difficulty, reset variables and update maze and positions.
        self.win.cell_size = min(self.win.board_size[1] // len(self.maze.mazearray[0]), self.win.board_size[0] // len(self.maze.mazearray))

        ## Set Variables
        Display.display_maze.count = 0.0 ## Iteration count
        Display.display_solution.animationInt = 10 ## Current solution path (Starts at ten, then increases)
        Display.display_solution.count = 0.0 ## Iteration count
        Display.display_win.animationInt = 0 ## Animation frame
        Display.display_win.count = 0.0 ## Iteration count

        self.loop = "play"


    def play_loop(self):
        self.loop = "play"
        for event in game.event.get():
            if event.type == game.QUIT:
                    self.loop = False
                    game.quit()
                    exit()
            elif event.type == game.KEYDOWN:
                if event.key == game.K_SPACE:
                    self.loop = "solve"
                    return
                else:
                    self.maze.mazearray = self.P1.update(event.key)
        updateRect = Display.display_maze(self.win, self.maze.mazearray)
        if len(self.maze.mazearray) < Display.display_maze.count: updateRect = Display.display_player(self.win, self.P1)  # Draw the player on the maze
        if self.P1.win:
            self.loop = "win"
        return updateRect

    def solve_loop(self):
        solutionTuple = (0, 0)
        solutionTuple = MazeSol.solveMaze(self.maze.mazearray, self.maze.get_start())
        for event in game.event.get():
            if event.type == game.QUIT:
                    self.loop = False
                    game.quit()
                    exit()
            elif event.type == game.KEYDOWN:
                if event.key == game.K_SPACE:
                    self.loop = "play"
                    return
        updateRect = Display.display_solution(self.win, solutionTuple[1])
        Display.display_player(self.win, self.P1)  # Draw the player on the maze
        return updateRect  # Update the display

    def win_loop(self):
        for event in game.event.get():
            if event.type == game.QUIT:
                self.loop = False
                game.quit()
                exit()
        Display.display_player(self.win, self.P1) # Draw the player on the maze
        updateRect, animation = Display.display_win(self.win, self.maze.mazearray)
        if not animation:
            self.win.fill((0, 0, 0), self.win.board)
            game.display.flip()
            self.next_level()
        return updateRect

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(5000)
    mainFrame = mainFrame()
    mainFrame.loop = "next_level"
    mainFrame.main()