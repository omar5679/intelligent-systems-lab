from Node import Node

def get_neighbors(current: Node, maze, cost_move,
                  initial_state, goal_state):
    
    border_up = len(maze)
    border_down = -1
    border_right = len(maze[0])
    border_left = -1
    neighbors = []
    cord_x = current.coordinates[0]
    cord_y = current.coordinates[1]
    val = current.get_f_value()

    if (current.coordinates[0] - 1 > border_left):
        neighbors.append(Node((cord_x - 1, cord_y), val + cost_move,
                              initial_state, goal_state))
        
    if (current.coordinates[0] + 1 < border_right):
        neighbors.append(Node((cord_x + 1, cord_y), val + cost_move,
                              initial_state, goal_state))
    
    if (current.coordinates[1] - 1 > border_down):
        neighbors.append(Node((cord_x - 1, cord_y), val + cost_move,
                              initial_state, goal_state))
    
    if (current.coordinates[1] + 1 > border_up):
        neighbors.append(Node((cord_x - 1, cord_y), val + cost_move,
                              initial_state, goal_state))
        
    return neighbors
        

def a_star(maze, initial_state, goal_state):

    cost_move = 10
    closed_set = []
    open_set = list(Node(initial_state, initial_state, goal_state))

    while (len(open_set) != 0):
        
        current : Node = min(open_set)

        if (current.coordinates == goal_state):
            return #reconstruct_path(initial_)
        
        open_set.remove(current)

        closed_set.append(current)

        for neighbor in get_neighbors(current, maze, cost_move,
                                     initial_state, goal_state):
            
            if neighbor in closed_set:
                continue
            
            if neighbor not in open_set or 
