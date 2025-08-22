import heapq
import math

# utilities
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1),          (0, 1),
              (1, -1), (1, 0), (1, 1)]

def heuristic(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def is_valid(x, y, grid):
    n = len(grid)
    return 0 <= x < n and 0 <= y < n and grid[x][y] == 0

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current)
    return path[::-1]

# BFS
def best_first_search(grid):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    pq = [(heuristic(start, goal), start)]
    visited = set()
    came_from = {}

    while pq:
        i, current = heapq.heappop(pq)
        if current == goal:
            path = reconstruct_path(came_from, current)
            return len(path), path

        if current in visited:
            continue
        visited.add(current)

        for dx, dy in DIRECTIONS:
            nx, ny = current[0] + dx, current[1] + dy
            if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                came_from[(nx, ny)] = current
                heapq.heappush(pq, (heuristic((nx, ny), goal), (nx, ny)))

    return -1, []

# A* Search
def a_star_search(grid):
    n = len(grid)
    start, goal = (0, 0), (n - 1, n - 1)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []

    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    pq = [(f_score[start], start)]
    came_from = {}

    while pq:
        i, current = heapq.heappop(pq)

        if current == goal:
            path = reconstruct_path(came_from, current)
            return len(path), path

        for dx, dy in DIRECTIONS:
            nx, ny = current[0] + dx, current[1] + dy
            if not is_valid(nx, ny, grid):
                continue

            tentative_g = g_score[current] + 1
            if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                came_from[(nx, ny)] = current
                g_score[(nx, ny)] = tentative_g
                f_score[(nx, ny)] = tentative_g + heuristic((nx, ny), goal)
                heapq.heappush(pq, (f_score[(nx, ny)], (nx, ny)))

    return -1, []


if __name__ == "__main__":
    grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0]
]

    bfs_len, bfs_path = best_first_search(grid)
    print(f"Best First Search -> Path length: {bfs_len}, Path: {bfs_path if bfs_len != -1 else ''}")
    astar_len, astar_path = a_star_search(grid)
    print(f"A* Search -> Path length: {astar_len}, Path: {astar_path if astar_len != -1 else ''}")


# Best First Search -> Path length: 10, Path: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (2, 3), (3, 2), (4, 3), (4, 4)]
# A* Search -> Path length: 8, Path: [(0, 0), (1, 0), (2, 0), (3, 0), (4, 1), (4, 2), (4, 3), (4, 4)]
