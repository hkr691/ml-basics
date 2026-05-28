from collections import deque

class GetRightMostNodes:
  def right_nodes(self, root):
    if not root:
      return []
    
    queue = deque([root])
    res = []
    
    while queue:
      queue_len = len(queue)
      rightMost = None
      
      for _ in range(queue_len):
        curr_node = queue.popleft()
        rightMost = curr_node.val
        
        if curr_node.left:
          queue.append(curr_node.left)
        if curr_node.right:
          queue.append(curr_node.right)
      
      res.append(rightMost)
    return res
        
