"""
Binary Tree Module with Iterative Methods

This module provides an implementation of a binary tree using iterative methods
for various tree operations.

Classes:
    - Node: Represents a single node in the binary tree, containing a value and
      left/right child nodes.
    - BinaryTreeIterativeImpl: Manages the binary tree and includes methods for
      insertion, traversal (inorder, preorder, postorder),
      calculating tree diameter, finding minimum and maximum depth, checking symmetry,
      converting a sorted array to a balanced BST,  and inverting the tree.

Usage Example:
    bt = BinaryTreeIterativeImpl()
    bt.insert(10)
    bt.insert(5)
    bt.insert(20)
    bt.insert(3)
    bt.insert(7)
    bt.insert(15)
    bt.insert(30)

    print("Inorder Traversal:", bt.inorder())
    print("Preorder Traversal:", bt.preorder())
    print("Postorder Traversal:", bt.postorder())
    print("Tree Diameter:", bt.calculate_tree_diameter(bt.root))
    print("Min Depth:", bt.min_depth(bt.root))
    print("Max Depth:", bt.maxDepth(bt.root))
    print("Is Symmetric:", bt.is_symmetric(bt.root))
    sorted_array = [1, 2, 3, 4, 5, 6, 7]
    bst_root = bt.convert_sorted_array_to_bst(sorted_array)
    inverted_tree_root = bt.invertTree(bt.root)
"""

from collections import deque
from typing import Optional, List


class Node:
    """
    Represents a single node in the binary tree.

    Attributes:
        left (Node): The left child node.
        right (Node): The right child node.
        value (int): The value stored in the node.
    """

    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinaryTreeIterativeImpl:
    """
    BinaryTreeIterativeImpl manages a binary tree using iterative methods 
    for various tree operations.

    Methods:
        - insert(key): Inserts a key into the binary tree.
        - inorder(): Performs an inorder traversal of the tree.
        - preorder(): Performs a preorder traversal of the tree.
        - postorder(): Performs a postorder traversal of the tree.
        - calculate_tree_diameter(root): Calculates the diameter of the tree.
        - min_depth(root): Finds the minimum depth of the tree.
        - maxDepth(root): Finds the maximum depth of the tree.
        - is_symmetric(root): Checks if the tree is symmetric.
        - convert_sorted_array_to_bst(nums): Converts a sorted array to a balanced
          binary search tree.
        - invertTree(root): Inverts the binary tree.
    """

    def __init__(self):
        self.root = None
        self.max_diameter = 0

    def insert(self, key: int):
        """
        Inserts a key into the binary tree.

        Args:
            key (int): The value to be inserted into the tree.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node: Optional[Node], key: int) -> None:
        """
        Helper method for insert, finds the correct position to insert the key iteratively.

        Args:
            node (Optional[Node]): The node to start the search from.
            key (int): The value to be inserted into the tree.
        """
        current = node
        while current:
            if key < current.value:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right

    def inorder(self):
        """
        Performs an inorder traversal of the tree.

        Returns:
            List[int]: A list of values from the tree in inorder sequence.
        """
        result = []
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.value)
            current = current.right
        return result

    def preorder(self):
        """
        Performs a preorder traversal of the tree.

        Returns:
            List[int]: A list of values from the tree in preorder sequence.
        """
        result = []
        if self.root is None:
            return result
        stack = [self.root]
        while stack:
            current = stack.pop()
            result.append(current.value)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result

    def postorder(self):
        """
        Performs a postorder traversal of the tree.

        Returns:
            List[int]: A list of values from the tree in postorder sequence.
        """
        result = []
        if self.root is None:
            return result
        stack1 = [self.root]
        stack2 = []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        while stack2:
            result.append(stack2.pop().value)
        return result

    def calculate_tree_diameter(self) -> int:
        """
        Calculates the diameter of the tree.

        Args:

        Returns:
            int: The diameter of the tree.
        """
        if not self.root:
            return 0

        max_diameter = 0
        node_height = {}
        stack = [(self.root, False)]

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

    def min_depth(self) -> int:
        """
        Finds the minimum depth of the tree.

        Args:

        Returns:
            int: The minimum depth of the tree.
        """
        if not self.root:
            return 0

        queue = deque([(self.root, 1)])

        while queue:
            node, depth = queue.popleft()

            is_leaf_node = not node.left and not node.right

            if is_leaf_node:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

    def max_depth(self) -> int:
        """
        Finds the maximum depth of the tree.

        Args:

        Returns:
            int: The maximum depth of the tree.
        """
        if not self.root:
            return 0

        stack = [(self.root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()

            max_depth = max(max_depth, depth)

            if node.right:
                stack.append((node.right, depth + 1))

            if node.left:
                stack.append((node.left, depth + 1))

        return max_depth

    def is_symmetric(self) -> bool:
        """
        Checks if the tree is symmetric.

        Args:

        Returns:
            bool: True if the tree is symmetric, False otherwise.
        """
        if not self.root:
            return False

        stack = [self.root.left, self.root.right]

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

    def convert_sorted_array_to_bst(self, nums: List[int]) -> Optional[Node]:
        """
        Converts a sorted array to a balanced binary search tree.

        Args:
            nums (List[int]): The sorted array.

        Returns:
            Optional[Node]: The root node of the balanced binary search tree.
        """
        if not nums:
            return None

        stack = []

        mid = len(nums) // 2 if len(nums) % 2 != 0 else (len(nums) // 2) - 1
        new_root = Node(nums[mid])

        stack.append((new_root, 0, len(nums) - 1))

        while stack:
            node, left, right = stack.pop()
            mid = (left + right) // 2

            # Left child
            if mid - 1 >= left:
                left_mid = (left + mid - 1) // 2
                node.left = Node(nums[left_mid])
                stack.append((node.left, left, mid - 1))

            # Right child
            if mid + 1 <= right:
                right_mid = (mid + 1 + right) // 2
                node.right = Node(nums[right_mid])
                stack.append((node.right, mid + 1, right))
        self.root = new_root
        return self.root

    def invert_tree(self) -> Optional[Node]:
        """
        Inverts the binary tree.

        Returns:
            Optional[Node]: The root node of the inverted tree.
        """
        if not self.root:
            return None

        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return self.root
