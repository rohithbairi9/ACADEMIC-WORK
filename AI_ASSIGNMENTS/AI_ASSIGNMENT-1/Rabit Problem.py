
class RabbitState:
    def __init__(self, state):
        self.state = state

    def __eq__(self, other):
        return isinstance(other, RabbitState) and self.state == other.state

    def __hash__(self):
        return hash(tuple(self.state))

    def __str__(self):
        return ''.join(self.state)

    def goalTest(self):
        return self.state == ['L', 'L', 'L', '_', 'R', 'R', 'R']

    def moveGen(self):
        next_states = []
        idx = self.state.index('_')
        directions = [-1, -2, 1, 2]
        for d in directions:
            new_idx = idx + d
            if 0 <= new_idx < 7:
                if abs(d) == 1 or (abs(d) == 2 and self.state[idx + d // 2] != '_'):
                    new_state = self.state.copy()
                    new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
                    next_states.append(RabbitState(new_state))
        return next_states

def reconstructPath(goal_node_pair, CLOSED):
    parent_map = {}
    for node, parent in CLOSED:
        parent_map[node] = parent
    
    path = []
    goal_node, parent = goal_node_pair
    path.append(goal_node)
    while parent is not None:
        path.append(parent)
        parent = parent_map[parent]
    
    return path


def removeSeen(children, OPEN, CLOSED):
    open_nodes = [node for node, parent in OPEN]
    closed_nodes = [node for node, parent in CLOSED]
    new_nodes = [c for c in children if c not in open_nodes and c not in closed_nodes]
    return new_nodes
    

def bfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair
        
        if N.goalTest():
            print("Goal is found")
            path = reconstructPath(node_pair, CLOSED)
            path.reverse()
            for node in path:
                print(node, " -> ",end="")
            return
        else:
            CLOSED.append(node_pair)
            children = N.moveGen()
            new_nodes = removeSeen(children, OPEN, CLOSED)
            new_pairs = [(node, N) for node in new_nodes]
            OPEN = OPEN + new_pairs
    return []

#DFS
def dfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair
        
        if N.goalTest():
            print("Goal is found")
            path = reconstructPath(node_pair, CLOSED)
            path.reverse()
            for node in path:
                print(node, " -> ",end="")
            return
        else:
            CLOSED.append(node_pair)
            children = N.moveGen()
            new_nodes = removeSeen(children, OPEN, CLOSED)
            new_pairs = [(node, N) for node in new_nodes]
            OPEN = new_pairs + OPEN #LIFO
    return []



start_state = RabbitState(['R', 'R', 'R', '_', 'L', 'L', 'L'])

print("BFS:")
bfs(start_state)

print("\nDFS:")
dfs(start_state)




