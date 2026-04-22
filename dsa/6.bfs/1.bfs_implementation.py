from collections import deque

class BFS:
  def bfs(self, graph, start, target):
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
      node, path = queue.popleft()
      if node == target:
        return path
        
      for neighbor in node.neighbors:
        if neighbor not in visited:
          visited.add(neighbor)
          queue.append((neighbor, path + [neighbor]))
    return   
    
