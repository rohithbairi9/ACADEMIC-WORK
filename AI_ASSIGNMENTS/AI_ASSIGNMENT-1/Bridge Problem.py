class BridgeState:
    def __init__(self, Amogh, Ameya, Grandmother, Grandfather, time,umbrella_side):
        self.positions = {
            "Amogh": Amogh,
            "Ameya": Ameya,
            "Grandmother": Grandmother,
            "Grandfather": Grandfather
        }
        self.time = time
        self.umbrella_side=umbrella_side

    def __eq__(self, other):
        return self.positions == other.positions and self.time == other.time

    def __hash__(self):
        return hash((tuple(sorted(self.positions.items())), self.time,self.umbrella_side))

    def __str__(self):
        return f"{self.positions}, Time: {self.time}"

    def goalTest(self):
        return all(side == "right" for side in self.positions.values()) and self.time <= 60

    def moveGen(self):
        children = []
        times = {
            "Amogh": 5,
            "Ameya": 10,
            "Grandmother": 20,
            "Grandfather": 25
        }

        candidates = [p for p, side in self.positions.items() if side == self.umbrella_side]

        if self.umbrella_side == "left":
            for i in range(len(candidates)):
                for j in range(i+1, len(candidates)):
                    p1, p2 = candidates[i], candidates[j]
                    new_positions = self.positions.copy()
                    new_positions[p1] = "right"
                    new_positions[p2] = "right"
                    new_time = self.time+ max(times[p1], times[p2])
                    if new_time <= 60:
                        child = BridgeState(**new_positions, time=new_time,umbrella_side="right")
                        children.append(child)
        else:
            for p in candidates:
                new_positions = self.positions.copy()
                new_positions[p] = "left"
                new_time = self.time + times[p]
                if new_time <= 60:
                    child = BridgeState(**new_positions, time=new_time,umbrella_side="left")
                    children.append(child)

        return children


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



start = BridgeState(
    Amogh="left",
    Ameya="left",
    Grandmother="left",
    Grandfather="left",
    time=0,
    umbrella_side="left"
)
print("Bridge Problem - BFS")
bfs(start)

print("\nBridge Problem - DFS")
dfs(start)
