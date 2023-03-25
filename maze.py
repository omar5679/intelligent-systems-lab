from algorithm import AStar
from generate_maze import generate_maze, print_maze, update_maze

def main():
    
    a_star = AStar()
    maze, init_state, goal_state = generate_maze()
    path = a_star.algorithm(maze, init_state, goal_state)

    print_maze(maze)

    updated_maze = update_maze(maze, path)
    print('\n\n\n')
    print_maze(updated_maze)
   

if __name__ == '__main__':
    main()
