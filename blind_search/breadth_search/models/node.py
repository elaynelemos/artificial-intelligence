class Node:
    def __init__(self, state, father=None, action, path_cost):
        self.state = state
        self.father = father
        self.action = action
        self.path_cost = path_cost

    def son_node(self, problem, action):
        son = Node(
            problem.result(self.state, action),
            self,
            action,
            self.path_cost + problem.step_cost(self.state, action))

        return son

