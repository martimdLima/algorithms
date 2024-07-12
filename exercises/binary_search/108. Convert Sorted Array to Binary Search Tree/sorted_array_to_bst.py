# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Recursive Approach
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_tree_recursive(sorted_list, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            node = TreeNode(sorted_list[mid])

            node.left = build_tree_recursive(sorted_list, start, mid - 1)
            node.right = build_tree_recursive(sorted_list, mid + 1, end)

            return node

        self.root = build_tree_recursive(nums, 0, len(nums) - 1)

    # Iterative Approach
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        stack = []

        mid = len(nums) // 2 if len(nums) % 2 != 0 else (len(nums) // 2) - 1
        root = TreeNode(nums[mid])

        stack.append((root, 0, len(nums) - 1))

        while stack:
            node, left, right = stack.pop()
            mid = (left + right) // 2

            # Left child
            if mid - 1 >= left:
                left_mid = (left + mid - 1) // 2
                node.left = TreeNode(nums[left_mid])
                stack.append((node.left, left, mid - 1))

            # Right child
            if mid + 1 <= right:
                right_mid = (mid + 1 + right) // 2
                node.right = TreeNode(nums[right_mid])
                stack.append((node.right, mid + 1, right))

        return root
