class PathSum:
  def get_path(self, root, target):
    if not root:
      return []
    
    def backtrack(node, path, total):
      if not node:
        return
      
      
      path.append(node.val)
      total += node.val
      if total > target: #prune only when there are positive nodes in the tree
        path.pop()
        return
      
      if not node.left and not node.right:
        if total == target:
          result.append(path[:])
      else:
        backtrack(node.left, path, total)
        backtrack(node.right, path, total)
      path.pop()
    
    result = []
    backtrack(root, [], 0)
    return result
