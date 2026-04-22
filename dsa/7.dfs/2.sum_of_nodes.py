from collections import deque
class SumOfNodes:
    def sum_of_tree_nodes(self, node):
        if not node:
            return 0
        return node.val + self.sum_of_tree_nodes(node.left) + self.sum_of_tree_nodes(node.right)
        
    def sum_of_nodes_iterative(self, root):
        if not root:
            return 0
        stack = [root]
        total_sum = 0
        
        while stack:
            node = stack.pop()
            total_sum += node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return total_sum
    
    def sum_of_nodes_bfs(self, root):
        if not root:
            return 0
        queue = deque([root])
        total_sum = 0
        
        while queue:
            node = queue.popleft()
            total_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return total_sum
