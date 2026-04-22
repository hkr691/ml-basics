class Solution:
    def levelSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        nodes = []
        queue = deque([root])

        while queue:
            # start of a new level here
            level_size = len(queue)
            sum_ = 0

            # process all nodes in the current level
            for i in range(level_size):
                node = queue.popleft()
                sum_ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # we are at the end of the level,
            # add the sum of the nodes to the output list
            nodes.append(sum_)

        return nodes
