class GoodNodes:
  def get_good_nodes(self, root):
    def dfs(root, max_):
      if not root:
        return 0
      
      count = 0      
      if root.val >= max_:
        count += 1
        max_ = root.val
      
      left = dfs(root.left, max_)
      right = dfs(root.right, max_)
      
      return count + left + right
    return dfs(root, -float("inf"))
