import pygame as game
import pygame.freetype as freetype
import numpy as np
import Player

class window:
    def __init__(self, caption: str = "Pygame", board: int = 700, side_menu: int = 30):
        self.display_size = (board+side_menu, board)
        self._display = game.display.set_mode(self.display_size) ## Init game.display as _display
        game.display.set_caption(caption)
        self.side_menu_size = (board, board)
        self.side_menu_topcorner = (board, 0)
        self.side_menu = game.Surface(self.side_menu_size)
        self.board_size = (board, board)
        self.board = game.Surface(self.board_size)
        self.cell_size = 0

    def fill(self, color: tuple, surface: game.Surface):
        return surface.fill(color)

    def flip(self):
        return game.display.flip()
    
    def update(self, rect: game.rect=None):
        self._display.blit(self.board, (0, 0))
        self._display.blit(self.side_menu, self.side_menu_topcorner)
        return game.display.update(rect)


def main():
    win = init_display()
    clock = game.time.Clock()

    # Example: Set cell_size for testing
    win.cell_size = 20

    # Example: Create a dummy maze for display
    maze = np.zeros((win.board_size[0] // win.cell_size, win.board_size[1] // win.cell_size), dtype=int)
    maze[0, 0] = 10  # Start
    maze[-1, -1] = 2  # End
    maze[1:3, 1:3] = 1  # Wall

    display_maze.count = 0

    running = True
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False

        win.fill((0, 0, 0), win.board)
        win.fill((50, 50, 50), win.side_menu)
        
        # --- Draw the maze onto the board surface ---
        display_maze(win, maze)
        
        
        win.flip()  # or win.update()

        clock.tick(60)

    game.quit()


def init_display(caption: str = "Labpy", H: int = 700, side: int = 30):
    """Initalize the display and function attributes.

    Args:
        caption (str, optional): The caption for the pygame window. Defaults to "Labpy".
        H (int, optional): The height of the pygame window. Defaults to 700.
        side (int, optional): The width of the sidemenu in the pygame window. Defaults to 30.

    Returns:
        _type_: The pygame window object.
    """
    game.init()
    win = window(caption, H, side)

    display_win.last_update = game.time.get_ticks()
    display_maze.last_update = game.time.get_ticks()

    return win

def display_maze(win: window, maze: np.array):
    """Displays the maze with a nice animation until completely loaded.

    Args:
        win (window): The window object representing the game display.
        maze (np.array): The np.array representing the maze.
    """
    now = game.time.get_ticks()
    # Only update animationInt every 50 ms (20 times per second)
    if now - display_maze.last_update > 50:
        display_maze.count += 1
        display_maze.last_update = now
    updateRect = game.Rect(0, 0, 600, display_maze.count*win.cell_size)
    for y, row in enumerate(maze):
        if y <= display_maze.count:
            for x, cell in enumerate(row):
                rect = game.Rect(x * win.cell_size, y * win.cell_size, win.cell_size, win.cell_size)
                if cell == 1:  # Wall
                    game.draw.rect(win.board, (0, 0, 0), rect)
                elif cell == 0:  # Path
                    game.draw.rect(win.board, (255, 255, 255), rect)
                elif cell == 10:  # Start
                    game.draw.rect(win.board, (0, 255, 0), rect)
                elif cell == 2:  # End
                    game.draw.rect(win.board, (255, 0, 0), rect)
    return updateRect

def display_solution(win: window, solution: np.array):
    if len(solution) > display_solution.count:
        display_solution.count += 1/2
    if display_solution.count.is_integer():
        display_solution.animationInt += 1
    updateRects = []
    for y, row in enumerate(solution):     
        for x, cell in enumerate(row):
            rect = game.Rect(x *win.cell_size, y *win.cell_size,win.cell_size,win.cell_size)
            if cell == 1:  # Wall
                game.draw.rect(win.board, (0, 0, 0), rect)
            elif cell == 0 or cell > display_solution.animationInt:  # Path or Unanimated solution
                game.draw.rect(win.board, (255, 255, 255), rect)
            elif cell == 10:  # Start
                game.draw.rect(win.board, (0, 255, 0), rect)
            elif cell == 2:  # End
                game.draw.rect(win.board, (255, 0, 0), rect)
            elif cell == 4 or (cell >= 10 and cell <= display_solution.animationInt): # Solution
                game.draw.rect(win.board, (0, 255, 255), rect)
                if cell == display_solution.animationInt or cell == 4:
                    updateRects.append(rect)
    return updateRects


def display_player(win: window, P1: Player.player):
    """_summary_

    Args:
        win (window): The window object representing the game display.
        player_pos (dict): The position of the player in the maze.
    """
    y, x = P1.position
    rect = game.Rect((x *win.cell_size)-win.cell_size, (y *win.cell_size)-win.cell_size,win.cell_size*3,win.cell_size*3)
    lastrect = game.Rect(P1.path[-2][1] *win.cell_size, P1.path[-2][0] *win.cell_size,win.cell_size,win.cell_size) if len(P1.path) > 1 else (game.Rect(P1.path[-1][1] *win.cell_size, P1.path[-1][0] *win.cell_size,win.cell_size,win.cell_size) if P1.path else None)
    game.draw.circle(win.board, (0, 0, 255), rect.center,win.cell_size/3)  # Draw player in blue
    return [rect, lastrect]

def display_win(win: window, maze: np.array):
    now = game.time.get_ticks()
    # Only update animationInt every 50 ms (20 times per second)
    if now - display_win.last_update > 50:
        display_win.animationInt += 1
        display_win.last_update = now
    updateRect = game.Rect(0, 0, win.board_size[0], display_win.animationInt*win.cell_size)
    game.draw.rect(win.board, (0, 0, 0), updateRect)
    running = display_win.animationInt != len(maze)
    win.fill((50, 50, 50), win.side_menu)
    return updateRect, running




if __name__ == "__main__":
    main()