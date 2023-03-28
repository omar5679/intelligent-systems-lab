from algorithm import AStar
from generate_maze import generate_maze, update_maze, print_maze_to_file

def main():

    a_star = AStar()
    maze, init_state, goal_state = generate_maze()
    path = a_star.algorithm(maze, init_state, goal_state)

    updated_maze = update_maze(maze, path)
    print_maze_to_file(updated_maze, 'maze.txt')
       

if __name__ == '__main__':
    main()
