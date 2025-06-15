import pygame as game
import pygame.freetype as freetype
import numpy as np
import Player

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

    display_win.last_update = game.time.get_ticks()

    return win

def display_maze(maze: np.array, cell_size: int):
    """_summary_

    Args:
        maze (np.array): The np.array representing the maze.
        cell_size (int): The size of each cell in the maze.
    """
    if len(maze) > display_maze.count:
        display_maze.count += 1/(2) ## Count the iterations of this func for a nice animation
    updateRect = game.Rect(len(maze[0]) * cell_size, display_maze.count * cell_size, width, cell_size)
    for y, row in enumerate(maze):
        if y <= display_maze.count:
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


def display_player(P1: Player.player, cell_size: int):
    """_summary_

    Args:
        player_pos (dict): The position of the player in the maze.
        cell_size (int): The size of each cell in the maze.
    """
    y, x = P1.position
    rect = game.Rect((x * cell_size)-cell_size, (y * cell_size)-cell_size, cell_size*3, cell_size*3)
    lastrect = game.Rect(P1.path[-2][1] * cell_size, P1.path[-2][0] * cell_size, cell_size, cell_size) if len(P1.path) > 1 else (game.Rect(P1.path[-1][1] * cell_size, P1.path[-1][0] * cell_size, cell_size, cell_size) if P1.path else None)
    game.draw.circle(win, (0, 0, 255), rect.center, cell_size/3)  # Draw player in blue
    return [rect, lastrect]

def display_win(maze: np.array, cell_size: int):
    now = game.time.get_ticks()
    # Only update animationInt every 50 ms (20 times per second)
    if now - display_win.last_update > 50:
        display_win.animationInt += 1
        display_win.last_update = now
    updateRect = game.Rect(0, display_win.animationInt * cell_size, cell_size * len(maze[0]), cell_size)
    game.draw.rect(win, (0, 0, 0), updateRect)
    running = display_win.animationInt != len(maze)
    return updateRect, running




if __name__ == "__main__":
    main()