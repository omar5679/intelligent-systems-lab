# Define the maze as a 2D list with 60 rows and 80 columns
import random
from colorama import Fore, Style

def generate_maze():
    maze = [['0' for j in range(80)] for i in range(60)]
    # Define the obstacle object
    obstacle = '*'
    initial = 'I'
    goal = 'G'

    initial_placerow = random.randint(0,59)
    initial_placecolumn = random.randint(0,79)

    goal_placerow = random.randint(0,59)
    goal_placecolumn = random.randint(0,79)

    # Fill the maze with 30% obstacles chosen randomly
    for i in range(60):
        for j in range(80):
            if random.random() < 0.3:  # 30% chance of adding an obstacle
                maze[i][j] = obstacle

    while maze[initial_placerow][initial_placecolumn] == obstacle:
        initial_placerow = random.randint(0, 59)
        initial_placecolumn = random.randint(0, 79)
    maze[initial_placerow][initial_placecolumn] = initial

    while maze[goal_placerow][goal_placecolumn] == obstacle:
        goal_placerow = random.randint(0, 59)
        goal_placecolumn = random.randint(0, 79)
    maze[goal_placerow][goal_placecolumn] = goal

    return maze, (initial_placecolumn, initial_placerow), (goal_placecolumn, goal_placerow)


def update_maze(maze, path):
    
    for state in path:
        if maze[state[1]][state[0]] != 'I' and maze[state[1]][state[0]] != 'G':
            maze[state[1]][state[0]] = '+'
    
    return maze


def print_maze(maze):
    # Print the maze
    goal_state_unreachable = True

    for i in range(60):
        for j in range(80):

            if (maze[i][j]) == '+':
                print(Fore.RED, end='')
                print(maze[i][j], end=' ')
                print(Style.RESET_ALL, end='')
                goal_state_unreachable = True
            elif maze[i][j] == 'I':
                print(Fore.GREEN, end='')
                print(maze[i][j], end=' ')
                print(Style.RESET_ALL, end='')
            elif maze[i][j] == 'G':
                print(Fore.BLUE, end='')
                print(maze[i][j], end=' ')
                print(Style.RESET_ALL, end='')
            else:
                print(maze[i][j], end=' ')
        print()

    if goal_state_unreachable:
        print('The goal state is unreachable from the initial state.')


def print_maze_to_file(maze, filename):
    with open(filename, 'w') as file:
        goal_state_unreachable = True
        # Write the maze to the file
        for i in range(60):
            for j in range(80):

                if (maze[i][j]) == '+':
                    file.write(maze[i][j] + ' ')
                    goal_state_unreachable = False
                elif maze[i][j] == 'I':
                    file.write(maze[i][j] + ' ')
                elif maze[i][j] == 'G':
                    file.write(maze[i][j] + ' ')
                else:
                    file.write(maze[i][j] + ' ')
            file.write('\n')

        if goal_state_unreachable:
            file.write('The goal state is unreachable from the initial state.')
