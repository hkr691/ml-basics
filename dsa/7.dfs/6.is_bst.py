# class TreeNode:
#     def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def validateBST(self, root: TreeNode) -> bool:
        # Your code goes here
        if not root:
            return True
        
        def dfs(node, min_, max_):
            #recursive case
            if not node:
                return True
            if node.val <= min_ or node.val >= max_:
                return False
            return dfs(node.left, min_, node.val) and dfs(node.right, node.val, max_)
        return dfs(root, -float("inf"), float("inf"))
