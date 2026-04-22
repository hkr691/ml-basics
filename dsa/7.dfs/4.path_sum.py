class PathSum:
  def get_pathsum(self, root, target):
    if not root:
      return False
    
    if not root.left and not root.right:
      return root.val == target
    target -= root.val
    return self.get_pathsum(root.left, target) or self.get_pathsum(root.right, target)
    
  def get_pathsum_iterative(self, root, target):
    if not root:
        return False
    
    stack = [(root, target)]
    
    while stack:
        node, current_target = stack.pop()
        
        if not node.left and not node.right:
            if current_target == node.val:
                return True
        
        if node.right:
            stack.append((node.right, current_target - node.val))
        if node.left:
            stack.append((node.left, current_target - node.val))
            
    return False
    
     
