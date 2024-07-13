# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        level_order_transversal = []

        while queue:
            node, level = queue.popleft()

            if len(level_order_transversal) - 1 < level:
                level_order_transversal.insert(level, [node.val])
            else:
                level_order_transversal[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        return level_order_transversal

    def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque([(root, 0)])
        level_order_transversal = defaultdict(list)

        while queue:
            node, level = queue.popleft()
            level_order_transversal[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        # Convert defaultdict to a list of lists
        result = [
            level_order_transversal[i] for i in range(len(level_order_transversal))
        ]
        return result
