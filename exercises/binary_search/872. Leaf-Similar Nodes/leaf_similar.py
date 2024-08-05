# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def postorder(root, leaf_nodes):
            if root:
                postorder(root.left, leaf_nodes)

                postorder(root.right, leaf_nodes)

                if root.left is None and root.right is None:
                    leaf_nodes.append(root.val)

        leaf_nodes_1 = []
        leaf_nodes_2 = []

        postorder(root1, leaf_nodes_1)
        postorder(root2, leaf_nodes_2)

        return leaf_nodes_1 == leaf_nodes_2

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leaf_generator(root):
            if root:
                if not root.left and not root.right:
                    yield root.val
                if root.left:
                    yield from leaf_generator(root.left)
                if root.right:
                    yield from leaf_generator(root.right)

        return list(leaf_generator(root1)) == list(leaf_generator(root2))
