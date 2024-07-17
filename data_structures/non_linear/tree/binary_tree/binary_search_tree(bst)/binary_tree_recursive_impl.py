"""
This module provides two classes for binary tree implementations: Node and BinaryTreeRecursiveImpl.

Node represents a single node in a binary tree with attributes for left child, right child, 
and a value.

BinaryTreeRecursiveImpl implements a binary tree using recursive methods for operations 
such as insertion, traversals (inorder, preorder, postorder), diameter calculation, depth
calculation, symmetry checking, conversion from sorted array to balanced BST, and tree inversion.

Classes:
    - Node: Represents a single node in the binary tree, containing a value and
      left/right child nodes.
    - BinaryTreeRecursiveImpl: Manages the binary tree and includes methods for
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

from typing import Optional, List


class Node:
    """
    Represents a single node in the binary tree.

    Attributes:
        left (Node): The left child node.
        right (Node): The right child node.
        val (int): The value stored in the node.
    """

    def __init__(self, key: int):
        self.left = None
        self.right = None
        self.val = key


class BinaryTreeRecursiveImpl:
    """
        Manages a binary tree using recursive methods for various tree operations.

    Methods:
        - insert(key): Inserts a key into the binary tree.
        - inorder(): Performs an inorder traversal of the tree.
        - preorder(): Performs a preorder traversal of the tree.
        - postorder(): Performs a postorder traversal of the tree.
        - calculate_tree_diameter(root): Calculates the diameter of the tree.
        - min_depth(root): Finds the minimum depth of the tree.
        - max_depth(root): Finds the maximum depth of the tree.
        - is_symmetric(root): Checks if the tree is symmetric.
        - convert_sorted_array_to_bst(nums): Converts a sorted array to a 
          balanced binary search tree.
        - invertTree(root): Inverts the binary tree.
    """

    def __init__(self):
        self.root = None
        self.max_diameter = 0

    def insert(self, key: int):
        """
        Inserts a key into the binary search tree.

        Args:
            key: The key to insert into the tree.
        """
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key: int):
        """
        Helper method to recursively insert a key into the binary search tree.

        Args:
            node (Node): The current node being considered.
            key: The key to insert into the tree rooted at 'node'.
        """
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def inorder_traversal(self, node: Optional[Node], result):
        """
        Performs an inorder traversal of the binary tree rooted at 'node'.

        Args:
            node (Node): The current node being visited.
            result (list): A list to store the keys in inorder traversal order.
        """
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right, result)

    def preorder_traversal(self, node: Optional[Node], result):
        """
        Performs a preorder traversal of the binary tree rooted at 'node'.

        Args:
            node (Node): The current node being visited.
            result (list): A list to store the keys in preorder traversal order.
        """
        if node:
            result.append(node.val)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)

    def postorder_traversal(self, node, result):
        """
        Performs a postorder traversal of the binary tree rooted at 'node'.

        Args:
            node (Node): The current node being visited.
            result (list): A list to store the keys in postorder traversal order.
        """
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.val)

    def inorder(self):
        """
        Returns a list of keys obtained by performing inorder traversal of the tree.
        """
        result = []
        self.inorder_traversal(self.root, result)
        return result

    def preorder(self):
        """
        Returns a list of keys obtained by performing preorder traversal of the tree.
        """
        result = []
        self.preorder_traversal(self.root, result)
        return result

    def postorder(self):
        """
        Returns a list of keys obtained by performing postorder traversal of the tree.
        """
        result = []
        self.postorder_traversal(self.root, result)
        return result

    def calculate_tree_diameter(self, root: Optional[Node]) -> int:
        """
        Calculates the diameter of the binary tree rooted at 'root'.

        Args:
            root (Node): The root node of the binary tree.

        Returns:
            int: The diameter of the binary tree.
        """
        self.max_diameter = 0

        def height(node: Optional[Node]):
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

    def min_depth(self, root: Optional[Node]) -> int:
        """
        Calculates the minimum depth of the binary tree rooted at 'root'.

        Args:
            root (Node): The root node of the binary tree.

        Returns:
            int: The minimum depth of the binary tree.
        """
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        if not root.left:
            return self.min_depth(root.right) + 1

        if not root.right:
            return self.min_depth(root.left) + 1

        return min(self.min_depth(root.left), self.min_depth(root.right)) + 1

    def max_depth(self, root: Optional[Node]) -> int:
        """
        Calculates the maximum depth of the binary tree rooted at 'root'.

        Args:
            root (Node): The root node of the binary tree.

        Returns:
            int: The maximum depth of the binary tree.
        """
        if root:
            left_depth = self.max_depth(root.left)
            right_depth = self.max_depth(root.right)
            return max(left_depth, right_depth) + 1
        return 0

    def is_symmetric(self) -> bool:
        """
        Checks if the binary tree rooted at 'root' is symmetric.

        Args:

        Returns:
            bool: True if the tree is symmetric, False otherwise.
        """

        def eval_nodes_symetry(left_node: Optional[Node], right_node: Optional[Node]):
            if not left_node and not right_node:
                return True

            if left_node and right_node and left_node.val == right_node.val:
                return eval_nodes_symetry(
                    left_node.left, right_node.right
                ) and eval_nodes_symetry(left_node.right, right_node.left)

            return False

        if not self.root:
            return True

        return eval_nodes_symetry(self.root.left, self.root.right)

    def convert_sorted_array_to_bst(self, nums: List[int]) -> Optional[Node]:
        """
        Constructs a balanced binary search tree from a sorted list of integers 'nums'.

        Args:
            nums (List[int]): A sorted list of integers.

        Returns:
            Optional[Node]: The root node of the constructed binary search tree.
        """

        def build_tree_recursive(sorted_list, start, end):
            if start > end:
                return None

            mid = (start + end) // 2
            node = Node(sorted_list[mid])

            node.left = build_tree_recursive(sorted_list, start, mid - 1)
            node.right = build_tree_recursive(sorted_list, mid + 1, end)

            return node

        self.root = build_tree_recursive(nums, 0, len(nums) - 1)
        return self.root

    def invert_tree(self, root: Optional[Node]) -> Optional[Node]:
        """
        Inverts the binary tree rooted at 'root'.

        Args:
            root (Node): The root node of the binary tree.

        Returns:
            Optional[Node]: The root node of the inverted binary tree.
        """
        if not root:
            return None

        left_node = self.invert_tree(root.left)
        right_node = self.invert_tree(root.right)

        root.left, root.right = right_node, left_node

        return root
