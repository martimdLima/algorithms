# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative approach
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            max_depth = max(max_depth, depth)

            if node.right:
                stack.append((node.right, depth + 1))

            if node.left:
                stack.append((node.left, depth + 1))

        return max_depth

    # Recursive approach
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            left_depth = maxDepth(root.left)
            right_depth = maxDepth(root.right)
            return max(left_depth, right_depth) + 1
        return 0
