import pygame as game
import numpy as np

height, width = 600, 600

def main():
    win = init_display()
    clock = game.time.Clock()

    running = True
    # Main game loop
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False

        win.fill((0, 0, 0))  # Fill the screen with black
        game.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 FPS

    game.quit()

def init_display(caption: str = "Labpy", H: int = height, W: int = width):
    """_summary_

    Args:
        caption (str, optional): The caption for the pygame window. Defaults to "Labpy".
        H (int, optional): The height of the pygame window. Defaults to HEIGHT.
        W (int, optional): The width of the pygame window. Defaults to WIDTH.

    Returns:
        _type_: The pygame window object.
    """
    game.init()
    global win
    win = game.display.set_mode((W, H))
    game.display.set_caption(caption)
    return win

def display_maze(maze: np.array, cell_size: int):
    """_summary_

    Args:
        maze (np.array): The np.array representing the maze.
        cell_size (int): The size of each cell in the maze.
        solution (list, optional): The mazes solution. Defaults to None.
    """
    print(f"Cell size: {cell_size}, Maze size: {len(maze)}x{len(maze[0])}, Maze: {maze}")
    for y, row in enumerate(maze):
        print(f"Row {y}: {row}")
        for x, cell in enumerate(row):
            print(f"Cell {x}: {cell}")
            rect = game.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if cell == 1:  # Wall
                game.draw.rect(win, (0, 0, 0), rect)
            elif cell == 0:  # Path
                game.draw.rect(win, (255, 255, 255), rect)
            elif cell == 3:  # Start
                game.draw.rect(win, (0, 255, 0), rect)
            elif cell == 2:  # End
                game.draw.rect(win, (255, 0, 0), rect)

def display_solution(solution: np.array, cell_size: int):
    """_summary_

    Args:
        solution (np.array): The solution path of the maze.
        cell_size (int): The size of each cell in the maze.
    """
    print(f"Cell size: {cell_size}, Maze size: {len(solution)}x{len(solution[0])}, Maze: {solution}")
    for y, row in enumerate(solution):
        print(f"Row {y}: {row}")
        for x, cell in enumerate(row):
            print(f"Cell {x}: {cell}")
            rect = game.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if cell == 1:  # Wall
                game.draw.rect(win, (0, 0, 0), rect)
            elif cell == 0:  # Path
                game.draw.rect(win, (255, 255, 255), rect)
            elif cell == 3:  # Start
                game.draw.rect(win, (0, 255, 0), rect)
            elif cell == 2:  # End
                game.draw.rect(win, (255, 0, 0), rect)

def display_player(player_pos: tuple, cell_size: int):
    """_summary_

    Args:
        player_pos (tuple): The position of the player in the maze.
        cell_size (int): The size of each cell in the maze.
    """
    x, y = player_pos
    rect = game.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    game.draw.circle(win, (0, 0, 255), rect.center, cell_size/3)  # Draw player in blue
    print(f"Player position: {player_pos}, Rect: {rect}")

if __name__ == "__main__":
    main()
# This code initializes a Pygame window and runs a simple event loop.
# It listens for the quit event to close the window and updates the display at 60 frames per second.
# The window is filled with a black color each frame.
# The code is structured to be run as a standalone script.
# It uses the Pygame library to create a graphical window.