from collections import deque

input_graph = [
  [0, 1, 0, 0, 0],
  [0, 1, 0, 1, 0],
  [0, 0, 0, 1, 0],
  [1, 1, 1, 1, 0],
  [0, 0, 0, 0, 0]
]

def bfs(graph):
    start = (0, 0)
    num_rows = len(graph) 
    num_cols =  len(graph[0])
    end = (num_rows - 1, num_cols - 1)
    
    # valid moves: up, down , left, right 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize queue (for bfs algorithm)
    q = deque([(start, 0)])
    
    # Algorithm optimization: marking visited nodes to prevent visiting 
    # nodes more than once.
    visited = set()
    visited.add(start)

    while q:
        current_location, distance = q.popleft()
        x, y = current_location

        # Check if we reached the end
        if current_location == end:
            return distance

        # Check neighbors for valid moves
        for dir_x, dir_y in directions:
            new_x, new_y = x + dir_x, y + dir_y

            # Check if move is valid, and it has not been visited yet.            
            if 0 <= new_x < num_rows and 0 <= new_y < num_cols and (new_x, new_y) not in visited:
                if graph[new_x][new_y] == 0:
                    q.append(((new_x, new_y), distance + 1))
                    visited.add((new_x, new_y))
    
    # unable to find path to end
    return -1


answer = bfs(input_graph)
print(f"shortest distance to end: {answer}")
