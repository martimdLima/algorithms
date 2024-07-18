# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def height(node: Optional[TreeNode]):
            if node is None:
                return 0

            left_node__height = height(node.left)
            right_node_height = height(node.right)

            current_nodes_diameter = left_node__height + right_node_height
            current_nodes_height = max(left_node__height, right_node_height) + 1
            self.max_diameter = max(self.max_diameter, current_nodes_diameter)

            return current_nodes_height

        height(root)

        return self.max_diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_diameter = 0
        node_height = {}
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if visited:
                left_height = node_height.get(node.left, 0)
                right_height = node_height.get(node.right, 0)
                node_height[node] = max(left_height, right_height) + 1
                max_diameter = max(max_diameter, left_height + right_height)
                continue

            stack.append((node, True))
            if node.left:
                stack.append((node.left, False))
            if node.right:
                stack.append((node.right, False))

        return max_diameter
