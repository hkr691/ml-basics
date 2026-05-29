from collections import deque

class MaxWidth:
  def get_max_width_of_tree(self, root):
    max_width = 0
    if not root:
      return max_width
    
    queue = deque([(root, 0)])
    
    while queue:
      level_len = len(queue)
      _, leftmost = queue[0]
      rightmost = leftmost
      
      for i in range(level_len):
        curr_node, pos = queue.popleft()
        if i == level_len - 1:
          rightmost = pos
        
        if curr_node.left:
          queue.append((curr_node.left, 2 * pos + 1))
        if curr_node.right:
          queue.append((curr_node.right, 2 * pos + 2))
        
      max_width = max(max_width, rightmost - leftmost + 1)
    return max_width
