from collections import deque

def bfs(root):
  if not root:
    return []
  
  queue = deque([root])
  result = []
  
  while queue:
    curr_node = queue.popleft()
    result.append(curr_node.val)
    
    if curr_node.left:
      queue.append(curr_node.left)
    if curr_node.right:
      queue.append(curr_node.right)
    
  return result
