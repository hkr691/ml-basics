# class TreeNode:
#     def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class ZigZagTreeTraversal:
  def zigzag_traversal(self, root):
    if not root:
      return []
    
    queue = deque([root])
    res = []
    left_to_right = True
    
    while queue:
      q_len = len(queue)
      curr_level_nodes = deque()
      
      for _ in range(q_len):
        curr_node = queue.popleft()
        if left_to_right: curr_level_nodes.append(curr_node.val)
        else: curr_level_nodes.appendleft(curr_node.val)
        
        if curr_node.left:
          queue.append(curr_node.left)
        if curr_node.right:
          queue.append(curr_node.right)
          
      res.append(list(curr_level_nodes))
      left_to_right = not left_to_right
    return res
