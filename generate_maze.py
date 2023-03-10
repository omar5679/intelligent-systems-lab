# Define the maze as a 2D list with 60 rows and 80 columns
import random

maze = [[0 for j in range(80)] for i in range(60)]
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

# Print the maze
for i in range(60):
    for j in range(80):
        print(maze[i][j], end=' ')
    print()
