from typing import List

class AdjacencyList:
  def create_adj_list(self, edges: List[List[int]], nodes: int):
    if not nodes or not edges:
      return {}
    
    adj_list = {i: [] for i in range(nodes)}
    
    for u, v in edges:
      adj_list[u].append(v)
      adj_list[v].append(u)
    
    return adj_list
  
  def dfs(self, adj_list):
    
    if not adj_list:
      return
    visited = set()
    
    def dfs_helper(node):
      if node in visited:
        return
        
      visited.add(node)
      for neighbor in adj_list[node]:
        if neighbor not in visited:
          dfs_helper(neighbor)
          
    for node in adj_list:
      if node not in visited:
        dfs_helper(node)
      
