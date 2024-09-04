from collections import deque
input_graph = [ 
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0] 
]

input_graph2 = [
  [0, 0, 1, 0],
  [1, 0, 1, 0],
  [0, 0, 0, 0],
  [0, 1, 1, 0],
  [0, 0, 0, 0]
]


def dfs(graph):
    start = (0,0)
    num_rows = len(graph) - 1
    num_cols = len(graph[0]) - 1
    end = (num_rows, num_cols)    
    
    q = deque() 
    q.append(start)
    
    while q:
        current_location = q.popleft()
        x = current_location[0]
        y = current_location[1]
        
        if current_location == end:
            return True

        if (x - 1 >= 0) and (graph[x - 1][y] == 0):
            q.append((x - 1, y))
        if (x + 1 <= num_rows) and (graph[x + 1][y] == 0):
            q.append((x + 1, y))
        if (y - 1 >= 0) and (graph[x][y - 1] == 0):
            q.append((x, y - 1))
        if (y + 1 <= num_cols) and (graph[x][y + 1] == 0):
            q.append((x,y + 1))



    return False


answer = dfs(input_graph)
print(answer)
assert answer == True

answer = dfs(input_graph2)
print(answer)
assert answer == True
