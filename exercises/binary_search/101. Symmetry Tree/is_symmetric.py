# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Using a stack
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return []

        stack = [root.left, root.right]

        while stack:
            left_node = stack.pop()
            right_node = stack.pop()

            if not left_node and not right_node:
                continue

            nodes_are_not_present = not left_node or not right_node

            if nodes_are_not_present:
                return False

            nodes_are_different = left_node.val != right_node.val

            if nodes_are_different:
                return False

            stack.append(left_node.left)
            stack.append(right_node.right)
            stack.append(left_node.right)
            stack.append(right_node.left)

        return True

    # Using recursion
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def evalNodesSymetry(
            left_node: Optional[TreeNode], right_node: Optional[TreeNode]
        ):
            if not left_node and not right_node:
                return True

            if left_node and right_node and left_node.val == right_node.val:
                return evalNodesSymetry(
                    left_node.left, right_node.right
                ) and evalNodesSymetry(left_node.right, right_node.left)

            return False

        if not root:
            return True

        return evalNodesSymetry(root.left, root.right)
