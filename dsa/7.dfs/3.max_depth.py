class MaxDepth:
  def get_max_depth(self, root):
    if not root:
      return 0
    
    left_depth = self.get_max_depth(root.left)
    right_depth = self.get_max_depth(root.right)
    return max(left_depth, right_depth) + 1
