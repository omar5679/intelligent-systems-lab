import math

class AStar:

    def __init__(self) -> None:
        self.g_cost = {}
        self.f_cost = {}
        self.parents = {}


    def heuristic(self, state: tuple, goal_state) -> int:
        return math.sqrt((goal_state[0] - state[0])**2 +
                         (goal_state[1] - state[1])**2)


    def reconstruct_path(self, current):
        path = []
        
        while current in self.parents.keys():
            path.append(current)
            current = self.parents[current]

        return path


    def get_neighbors(self, current: tuple, maze):
    
        border_up = len(maze)
        border_down = -1
        border_right = len(maze[0])
        border_left = -1
        neighbors = []
        cord_x = current[0]
        cord_y = current[1]
        # val = current.get_f_value()

        if (cord_x - 1 > border_left and maze[cord_y][cord_x -1] != '*'):
            neighbors.append((cord_x - 1, cord_y))
            
        if (cord_x + 1 < border_right and maze[cord_y][cord_x +1] != '*'):
            neighbors.append((cord_x + 1, cord_y))

        if (cord_y - 1 > border_down and maze[cord_y - 1][cord_x] != '*'):
            neighbors.append((cord_x, cord_y - 1))
        
        if (cord_y + 1 < border_up and maze[cord_y + 1][cord_x] != '*'):
            neighbors.append((cord_x, cord_y + 1))
            
        return neighbors


    def algorithm(self, maze, initial_state, goal_state):
        closed_set = set()
        open_set = set()
        open_set.add(initial_state)
        self.g_cost.update({initial_state: 0})
        self.f_cost.update({initial_state: self.g_cost[initial_state] + self.heuristic(initial_state, goal_state)})

        while len(open_set) != 0:
            current = min(open_set, key=lambda coords: self.f_cost[coords]) # will it work?

            if current == goal_state:
                return self.reconstruct_path(current)
            
            open_set.remove(current)
            closed_set.add(current)
            
            for neighbor in self.get_neighbors(current, maze):
                
                if neighbor in closed_set:
                    continue

                # I assumed that you can not move diagonally
                tentative_g = self.g_cost[current] + 10

                if (neighbor not in open_set or 
                    (tentative_g in self.g_cost.keys() and
                     tentative_g < self.g_cost[neighbor])):
                    
                    self.parents[neighbor] = current

                    self.g_cost[neighbor] = tentative_g
                    self.f_cost[neighbor] = self.g_cost[neighbor] + self.heuristic(neighbor, goal_state)

                    open_set.add(neighbor)

        return []



