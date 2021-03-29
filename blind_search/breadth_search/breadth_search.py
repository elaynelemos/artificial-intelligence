from models.node import Node
from models.edge import Edge

def width_search(problem, action):
    first_node = Node(state=problem.initial_state, action=action, path_cost=0)

    if problem.objective(first_node.state):
        return solution(first_node)

    search_edge = Edge(first_node)
    visited_nodes = []
    while True:
        if search_edge.is_empty():
            return 'failed'
        nd = search_edge.pop()
        visited_nodes.append(nd)

        for action in problem.actions(nd.state):
            son = nd.son_node(problem, action)
            if not(son in visited_nodes) or search_edge.nodes:
                if problem.objective(son.state):
                    return solution(son)
                search_edge.insert(son)


def solution(node):
    pass
