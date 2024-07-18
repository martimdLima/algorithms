# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Postorder traversal using a stack
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []
        visited = set()

        while stack:
            node = stack[-1]
            if (node.left is None and node.right is None) or node in visited:
                result.append(node.val)
                stack.pop()
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                visited.add(node)

        return result

    # Postorder traversal using Morris Traversal
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        current_node = root

        while current_node is not None:
            if current_node.right is None:
                result.append(current_node.val)
                current_node = current_node.left
            else:
                previous_node = current_node.right
                while previous_node.left is not None and previous_node.left != current_node:
                    previous_node = previous_node.left

                if previous_node.left is None:
                    result.append(current_node.val)
                    previous_node.left = current_node
                    current_node = current_node.right
                else:
                    previous_node.left = None
                    current_node = current_node.left

        result.reverse()
        return result
