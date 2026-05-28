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

def level_order(root):
  if not root:
    return []
  
  queue = deque([root])
  res = []
  
  while queue:
    curr_level = []
    for _ in range(len(queue)):
      curr_node = queue.popleft()
      curr_level.append(curr_node.val)
      
      if curr_node.left:
        queue.append(curr_node.left)
      if curr_node.right:
        queue.append(curr_node.right)
    res.append(curr_level)
  return res
