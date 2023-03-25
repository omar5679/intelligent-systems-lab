class Node:


    def __init__(self, coordinates: tuple, f_value, initial_state, goal_state) -> None:
        '''
        f_value - value already known distance from the goal node
        h_value - heuristic
        g_value - h_value + f_value
        '''
        self.coordinates = coordinates
        self.f_value = f_value
        self.h_value = self.calculate_h(initial_state, goal_state)
        self._g_value = self.g_value + f_value

    def reset_f_value(self, value):
        self.f_value = value
        self._g_value += self.f_value + self.g_value
    
    def get_g_value(self):
        return self._g_value
    
    def get_f_value(self):
        return self.f_value

    def calculate_h(init: tuple, goal: tuple):
        pass


    def heurisitc():
        pass

    def __lt__(self, other):
        return self.g_value < other.get_g_value
    

    def __gt__(self, other):
        return self.g_value > other.get_g_value
        
        