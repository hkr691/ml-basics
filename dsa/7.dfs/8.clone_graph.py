from typing import List, Dict
# class IntGraphNode:
#     def __init__(self, value, id, neighbors):
#         self.value = value
#         self.id = id
#         self.neighbors = neighbors

class CopyGraph:
  #return an adjacency list
  def copy_graph(self, node: IntGraphNode) -> Dict[int, List[int]]:
    
    adj_list = {}
    
    def dfs(curr_node):
      if curr_node.value in adj_list:
        return
      adj_list[curr_node.value] = [n.value for n in curr_node.neighbors]
      
      for neighbor in curr_node.neighbors:
        dfs(neighbor)

    dfs(node)
    return adj_list
