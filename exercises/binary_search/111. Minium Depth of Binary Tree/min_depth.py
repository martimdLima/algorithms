class Solution:
    # Iterative approach
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            is_leaf_node = not node.left and not node.right

            if is_leaf_node:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

    # Recursive approach
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not node:
            return 0

        if not node.left and not node.right:
            return 1

        if not node.left:
            return self.min_depth(node.right) + 1

        if not node.right:
            return self.min_depth(node.left) + 1

        return min(self.min_depth(node.left), self.min_depth(node.right)) + 1
