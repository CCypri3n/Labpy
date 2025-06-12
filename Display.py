import pygame as game
WIN = game.display()
HEIGHT, WIDTH = 800, 800
WIN.set_mode((WIDTH, HEIGHT))
WIN.set_caption("Labpy")

def main():

    game.init()
    clock = game.time.Clock()

    running = True
    # Main game loop
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False

        WIN.fill((0, 0, 0))  # Fill the screen with black
        game.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 FPS

    game.quit()

if __name__ == "__main__":
    main()
# This code initializes a Pygame window and runs a simple event loop.
# It listens for the quit event to close the window and updates the display at 60 frames per second.
# The window is filled with a black color each frame.
# The code is structured to be run as a standalone script.
# It uses the Pygame library to create a graphical window.