import random

# Define the size of the maze
ROWS = 60
COLS = 80

# Define the fraction of maze elements that will contain an obstacle
OBSTACLE_DENSITY = 0.3

# Define the possible states of the agent
EMPTY = ' '
OBSTACLE = '*'
INITIAL_STATE = 'I'
GOAL_STATE = 'G'
OPTIMAL_PATH = '+'

# Define the A* algorithm with a suitable heuristic function
def astar(maze, start, end):
    def heuristic(node):
        return abs(node[0]-end[0]) + abs(node[1]-end[1])
    
    # Initialize the open and closed sets
    open_set = {start}
    closed_set = set()
    
    # Initialize the dictionary to store the optimal path
    came_from = {}
    
    # Initialize the dictionary to store the cost of reaching each node
    g_score = {start: 0}
    
    # Initialize the dictionary to store the estimated cost of reaching the goal from each node
    f_score = {start: heuristic(start)}
    
    while open_set:
        # Find the node with the lowest estimated cost to the goal
        current = min(open_set, key=lambda x: f_score[x])
        
        # If we have reached the goal, return the optimal path
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        # Move the current node from the open set to the closed set
        open_set.remove(current)
        closed_set.add(current)
        
        # Explore the neighbors of the current node
        for neighbor in [(current[0]-1, current[1]), (current[0]+1, current[1]), (current[0], current[1]-1), (current[0], current[1]+1)]:
            # Check if the neighbor is valid and not already explored
            if 0 <= neighbor[0] < ROWS and 0 <= neighbor[1] < COLS and maze[neighbor[0]][neighbor[1]] != OBSTACLE and neighbor not in closed_set:
                # Calculate the cost of reaching the neighbor from the current node
                tentative_g_score = g_score[current] + 1
                
                # Add the neighbor to the open set if it is not already there
                if neighbor not in open_set:
                    open_set.add(neighbor)
                elif tentative_g_score >= g_score[neighbor]:
                    continue
                
                # Record the optimal path to the neighbor
                came_from[neighbor] = current
                
                # Record the cost of reaching the neighbor
                g_score[neighbor] = tentative_g_score
                
                # Record the estimated cost of reaching the goal from the neighbor
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
    
    # If we reach this point, there is no path from the start to the goal
    return None

# Create the maze
maze = [[EMPTY for j in range(COLS)] for i in range(ROWS)]

# Add obstacles to the maze
num_obstacles = int(ROWS * COLS * OBSTACLE_DENSITY)
for i in range(num_obstacles):
    row = random.randint(0, ROWS-1)
    col = random.randint(0, COLS-1)
    maze[row][col] = OBSTACLE

# Select the initial and goal states
while True:
    start = (random.randint(0, ROWS-1
