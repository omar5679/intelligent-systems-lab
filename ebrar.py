# Define the maze as a 2D list with 60 rows and 80 columns
import random
import sys
import math
from colorama import Fore, Style


def generate_maze():
    maze = [['' for j in range(80)] for i in range(60)]
    # Define the obstacle object
    obstacle = '*'
    initial = 'I'
    goal = 'G'

    initial_placerow = random.randint(0, 59)
    initial_placecolumn = random.randint(0, 79)

    goal_placerow = random.randint(0, 59)
    goal_placecolumn = random.randint(0, 79)

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
            maze[state[1]][state[0]] = 'P'

    return maze


def print_maze(maze):
    # Print the maze
    for i in range(60):
        for j in range(80):

            if (maze[i][j]) == 'P':
                print(Fore.RED, end='')
                print(maze[i][j], end=' ')
                print(Style.RESET_ALL, end='')
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

class AStar:

    def __init__(self) -> None:
        self._g_cost = {}
        self._f_cost = {}
        self._parents = {}
        self._obstacle = '*'

    def _heuristic(self, state: tuple, goal_state) -> int:
        return math.sqrt((goal_state[0] - state[0]) ** 2 +
                         (goal_state[1] - state[1]) ** 2)

    def _reconstruct_path(self, current):
        path = []

        while current in self._parents.keys():
            path.append(current)
            current = self._parents[current]

        return path

    def _get_neighbors(self, current: tuple, maze):

        border_up = len(maze)
        border_down = -1
        border_right = len(maze[0])
        border_left = -1
        neighbors = []
        cord_x = current[0]
        cord_y = current[1]

        if (cord_x - 1 > border_left and maze[cord_y][cord_x - 1] != self._obstacle):
            neighbors.append((cord_x - 1, cord_y))

        if (cord_x + 1 < border_right and maze[cord_y][cord_x + 1] != self._obstacle):
            neighbors.append((cord_x + 1, cord_y))

        if (cord_y - 1 > border_down and maze[cord_y - 1][cord_x] != self._obstacle):
            neighbors.append((cord_x, cord_y - 1))

        if (cord_y + 1 < border_up and maze[cord_y + 1][cord_x] != self._obstacle):
            neighbors.append((cord_x, cord_y + 1))

        return neighbors

    def algorithm(self, maze, initial_state, goal_state):
        closed_set = set()
        open_set = set()
        open_set.add(initial_state)
        self._g_cost.update({initial_state: 0})
        self._f_cost.update({initial_state: self._g_cost[initial_state] + self._heuristic(initial_state, goal_state)})

        while len(open_set) != 0:
            current = min(open_set, key=lambda coords: self._f_cost[coords])

            if current == goal_state:
                return self._reconstruct_path(current)

            open_set.remove(current)
            closed_set.add(current)

            for neighbor in self._get_neighbors(current, maze):

                if neighbor in closed_set:
                    continue

                # I assumed that you can not move diagonally
                tentative_g = self._g_cost[current] + 1

                if (neighbor not in open_set or
                        (tentative_g in self._g_cost.keys() and
                         tentative_g < self._g_cost[neighbor])):
                    self._parents[neighbor] = current

                    self._g_cost[neighbor] = tentative_g
                    self._f_cost[neighbor] = self._g_cost[neighbor] + self._heuristic(neighbor, goal_state)

                    open_set.add(neighbor)

        return []


def print_maze_to_file(maze, filename):
    with open(filename, 'w') as file:
        # Write the maze to the file
        for i in range(60):
            for j in range(80):

                if (maze[i][j]) == 'P':
                    file.write(maze[i][j])
                elif maze[i][j] == 'I':
                    file.write(maze[i][j])
                elif maze[i][j] == 'G':
                    file.write(maze[i][j])
                else:
                    file.write(maze[i][j] + ' ')
            file.write('\n')





def main():
    a_star = AStar()
    maze, init_state, goal_state = generate_maze()
    path = a_star.algorithm(maze, init_state, goal_state)

    #print_maze(maze)

    updated_maze = update_maze(maze, path)
    print('\n\n\n')
    #print_maze(updated_maze)

    maze, initial_state, goal_state = generate_maze()
    path = AStar().algorithm(maze, initial_state, goal_state)
    updated_maze = update_maze(maze, path)
    

    print_maze_to_file(updated_maze, 'maze.txt')

if __name__ == '__main__':
    main()
