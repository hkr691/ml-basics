class SumOfNodes:
    def sum_of_tree_nodes(self, node):
        if not node:
            return 0
        return node.val + self.sum_of_tree_nodes(node.left) + self.sum_of_tree_nodes(node.right)
