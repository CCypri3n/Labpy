import numpy as np
import Display as display
import MazeSolver as MazeSolver

def main():
    # Initialize the display
    display.init_display()

    # Create a maze
    maze = MazeSolver.create_maze(20, 20)

    # Solve the maze
    solution = MazeSolver.solve_maze(maze)

    # Display the maze and solution
    display.display_maze(maze, solution)

if __name__ == "__main__":
    main()