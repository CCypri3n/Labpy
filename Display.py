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
    """
    if len(maze) > display_maze.counter:
        display_maze.counter += 1/(5) ## Count the iterations of this func for a nice animation, replaces y
    updateRect = game.Rect(len(maze[0]) * cell_size, display_maze.counter * cell_size, width, cell_size)
    for y, row in enumerate(maze):
        if y <= display_maze.counter:
            for x, cell in enumerate(row):
                rect = game.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
                if cell == 1:  # Wall
                    game.draw.rect(win, (0, 0, 0), rect)
                elif cell == 0:  # Path
                    game.draw.rect(win, (255, 255, 255), rect)
                elif cell == 10:  # Start
                    game.draw.rect(win, (0, 255, 0), rect)
                elif cell == 2:  # End
                    game.draw.rect(win, (255, 0, 0), rect)
    return updateRect

def display_solution(solution: np.array, cell_size: int):
    if len(solution) > display_solution.count:
        display_solution.count += 1/2
    if display_solution.count.is_integer():
        display_solution.animationInt += 1
    updateRects = []
    for y, row in enumerate(solution):     
        for x, cell in enumerate(row):
            rect = game.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if cell == 1:  # Wall
                game.draw.rect(win, (0, 0, 0), rect)
            elif cell == 0 or cell > display_solution.animationInt:  # Path or Unanimated solution
                game.draw.rect(win, (255, 255, 255), rect)
            elif cell == 10:  # Start
                game.draw.rect(win, (0, 255, 0), rect)
            elif cell == 2:  # End
                game.draw.rect(win, (255, 0, 0), rect)
            elif cell == 4 or (cell >= 10 and cell <= display_solution.animationInt): # Solution
                game.draw.rect(win, (0, 255, 255), rect)
                if cell == display_solution.animationInt or cell == 4:
                    updateRects.append(rect)
    return updateRects


def display_player(player_pos: dict, cell_size: int):
    """_summary_

    Args:
        player_pos (dict): The position of the player in the maze.
        cell_size (int): The size of each cell in the maze.
    """
    x = player_pos["x"]
    y = player_pos["y"]
    rect = game.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
    game.draw.circle(win, (0, 0, 255), rect.center, cell_size/3)  # Draw player in blue
    return rect

def display_win(maze: np.array, cell_size: int):
    pass

if __name__ == "__main__":
    main()