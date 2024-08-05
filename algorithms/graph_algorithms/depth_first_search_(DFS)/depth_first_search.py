"""
This module provides implementations of Depth-First Search (DFS) methods for both
graphs and binary trees. The module includes a `TreeNode` class representing nodes
in a binary tree, and two main classes:

1. `DepthFirstForGraph`: Contains methods for iterative and recursive DFS traversals
   and searches in a graph represented by adjacency lists.

2. `DepthFirstForTree`: Offers various DFS traversals (in-order, pre-order, post-order)
   and search methods for binary trees, both iterative and recursive.
"""

from typing import Optional, List
from Collections import deque


class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
    -----------
    val : int
        The value stored in the node.
    left : Optional[TreeNode]
        A reference to the left child node, or None if no child exists.
    right : Optional[TreeNode]
        A reference to the right child node, or None if no child exists.

    Methods:
    --------
    __init__(val=0, left=None, right=None)
        Initializes a TreeNode with a given value, and optional left and right children.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DepthFirstForGraph:
    """
    Provides methods to perform Depth-First Search (DFS) on a graph.

    This class includes both iterative and recursive implementations for
    traversing and searching through graph structures represented as adjacency lists.
    """

    def dfs_iterative_graph(self, graph: dict, start: int) -> list:
        """
        Performs an iterative Depth-First Search (DFS) traversal on a graph.

        Args:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      The keys are node identifiers, and the values are lists of adjacent nodes.
        start (int): The starting node for the DFS traversal.

        Returns:
        list: A list of nodes in the order they were visited.

        Example:
        --------
        graph = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0, 4],
            3: [1, 5],
            4: [1, 2],
            5: [3]
        }
        >>> dfs_iterative_graph(graph, 0)
        [0, 2, 4, 1, 3, 5]
        """
        visited = set()
        stack = [start]
        dfs_order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                dfs_order.append(node)
                # Add neighbors in reverse order to visit them in the original order
                stack.extend(reversed(graph[node]))

        return dfs_order

    def dfs_recursive_graph(self, graph: dict, start: int, visited=None) -> list:
        """
        Performs a recursive Depth-First Search (DFS) traversal on a graph.

        Args:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      The keys are node identifiers, and the values are lists of adjacent nodes.
        start (int): The starting node for the DFS traversal.
        visited (set, optional): A set to track visited nodes.

        Returns:
        list: A list of nodes in the order they were visited.

        Example:
        --------
        graph = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0, 4],
            3: [1, 5],
            4: [1, 2],
            5: [3]
        }
        >>> dfs_recursive_graph(graph, 0)
        [0, 1, 3, 5, 4, 2]
        """
        if visited is None:
            visited = set()
        visited.add(start)
        dfs_order = [start]

        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs_order.extend(self.dfs_recursive_graph(graph, neighbor, visited))

        return dfs_order

    def dfs_search_graph_iterative(self, graph: dict, start: int, target: int) -> int:
        """
        Searches for a target element in a graph using iterative DFS.

        Args:
        graph (dict): The adjacency list of the graph.
        start (int): The starting node for the DFS traversal.
        target (int): The element to search for.

        Returns:
        int: The node identifier where the target is found, or None if not found.

        Example:
        --------
        graph = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0, 4],
            3: [1, 5],
            4: [1, 2],
            5: [3]
        }
        >>> dfs_search_graph(graph, 0, 5)
        5

        >>> dfs_search_graph(graph, 0, 6)
        None
        """
        visited = set()
        stack = [start]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                if node == target:
                    return node
                stack.extend(reversed(graph[node]))

        return None

    def dfs_search_graph_recursive(self, graph: dict, start: int, target: int) -> int:
        """
        Searches for a target element in a graph using recursive DFS.

        Args:
        graph (dict): The adjacency list of the graph.
        start (int): The starting node for the DFS traversal.
        target (int): The element to search for.

        Returns:
        int: The node identifier where the target is found, or None if not found.

        Example:
        --------
        graph = {
            0: [1, 2],
            1: [0, 3, 4],
            2: [0, 4],
            3: [1, 5],
            4: [1, 2],
            5: [3]
        }
        >>> dfs_search_graph_recursive(graph, 0, 5)
        5

        >>> dfs_search_graph_recursive(graph, 0, 6)
        None
        """

        def dfs(node, visited):
            if node == target:
                return node
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    result = dfs(neighbor, visited)
                    if result is not None:
                        return result
            return None

        visited = set()
        return dfs(start, visited)


class DepthFirstForTree:
    """
    A class containing various depth-first search (DFS) methods for traversing and searching a binary tree.

    Methods:
    ---------
    1. dfs_inorder_transversal_iterative(root: Optional[TreeNode]) -> List[int]:
       Performs an iterative in-order traversal of a binary tree and returns a list of node values in in-order sequence.

    2. dfs_inorder_transversal_recursive(root: Optional[TreeNode]) -> List[int]:
       Performs a recursive in-order traversal of a binary tree and returns a list of node values in in-order sequence.

    3. dfs_preorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
       Performs an iterative pre-order traversal of a binary tree and returns a list of node values in pre-order sequence.

    4. dfs_preorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
       Performs a recursive pre-order traversal of a binary tree and returns a list of node values in pre-order sequence.

    5. dfs_postorder_traversal_iterative(root: Optional[TreeNode]) -> List[int]:
       Performs an iterative post-order traversal of a binary tree and returns a list of node values in post-order sequence.

    6. dfs_postorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
       Performs a recursive post-order traversal of a binary tree and returns a list of node values in post-order sequence.

    7. dfs_inorder_search_recursive(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
       Performs a recursive in-order search to find and return the node containing a specific value.

    8. dfs_inorder_search_iterative(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
       Performs an iterative in-order search to find and return the node containing a specific value.

    9. dfs_preorder_search_recursive(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
       Performs a recursive pre-order search to find and return the node containing a specific value.

    10. dfs_preorder_search_iterative(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        Performs an iterative pre-order search to find and return the node containing a specific value.

    11. dfs_postorder_search_recursive(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        Performs a recursive post-order search to find and return the node containing a specific value.

    12. dfs_postorder_search_iterative(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        Performs an iterative post-order search to find and return the node containing a specific value.

    Each search method returns the node containing the target value or None if the target is not found. Each traversal method returns a list of node values in the respective traversal order.
    """

    def dfs_inorder_transversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an iterative in-order traversal of a binary tree.

        Args:
        root (TreeNode): The root node of the binary tree.

        Returns:
        list: A list of values of the nodes in the order they were visited (in-order).

        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)

        >>> dfs_inorder_transversal_iterative(root)
        [4, 2, 5, 1, 3, 6]
        """
        result = []
        stack = []
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result

    def dfs_inorder_transversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs a recursive in-order traversal of a binary tree.
    
        In-order traversal visits nodes in the following order:
        1. Left subtree
        2. Current node
        3. Right subtree
    
        Args:
        root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.
    
        Returns:
        List[int]: A list of node values in the order they were visited during the in-order traversal.
    
        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
    
        >>> dfs_inorder_transversal_recursive(root)
        [4, 2, 5, 1, 3, 6]
        """
        if root:
            return (
                self.dfs_inorder_transversal_recursive(root.left)
                + [root.val]
                + self.dfs_inorder_transversal_recursive(root.right)
            )
        else:
            return []

    def dfs_pretorder_traversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an iterative pre-order traversal of a binary tree.
    
        In pre-order traversal, nodes are visited in the following order:
        1. Current node
        2. Left subtree
        3. Right subtree
    
        Args:
        root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.
    
        Returns:
        List[int]: A list of node values in the order they were visited during the pre-order traversal.
    
        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
    
        >>> dfs_preorder_traversal_iterative(root)
        [1, 2, 4, 5, 3, 6]
        """
        if not root:
            return []

        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

        def dfs_preorder_traversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
            """
            Performs a recursive pre-order traversal of a binary tree.
    
            In pre-order traversal, nodes are visited in the following order:
            1. Current node
            2. Left subtree
            3. Right subtree
    
            Args:
            root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.
    
            Returns:
            List[int]: A list of node values in the order they were visited during the pre-order traversal.
    
            Example:
            --------
            # Tree structure:
            #      1
            #     / \
            #    2   3
            #   / \   \
            #  4   5   6
            root = TreeNode(1)
            root.left = TreeNode(2)
            root.right = TreeNode(3)
            root.left.left = TreeNode(4)
            root.left.right = TreeNode(5)
            root.right.right = TreeNode(6)
    
            >>> dfs_preorder_traversal_recursive(root)
            [1, 2, 4, 5, 3, 6]
            """

            def preorder(node):
                if not node:
                    return []
                return [node.val] + preorder(node.left) + preorder(node.right)

            return preorder(root)

    def dfs_postorder_traversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an iterative post-order traversal of a binary tree.
    
        In post-order traversal, nodes are visited in the following order:
        1. Left subtree
        2. Right subtree
        3. Current node
    
        Args:
        root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.
    
        Returns:
        List[int]: A list of node values in the order they were visited during the post-order traversal.
    
        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)
    
        >>> dfs_postorder_traversal_iterative(root)
        [4, 5, 2, 6, 3, 1]
        """
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

    def dfs_postorder_traversal_recursive(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs a recursive post-order traversal of a binary tree.

        In post-order traversal, nodes are visited in the following order:
        1. Left subtree
        2. Right subtree
        3. Current node

        Args:
        root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.

        Returns:
        List[int]: A list of node values in the order they were visited during the post-order traversal.

        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)

        >>> dfs_postorder_traversal_recursive(root)
        [4, 5, 2, 6, 3, 1]
        """

        def postorder(node):
            if not node:
                return []
            return postorder(node.left) + postorder(node.right) + [node.val]

        return postorder(root)

    def dfs_inorder_search_recursive(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Performs a recursive in-order search in a binary tree to find a node with a specific value.

        In in-order traversal, nodes are visited in the following order:
        1. Left subtree
        2. Current node
        3. Right subtree

        Args:
        root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.
        target (int): The value to search for in the tree.

        Returns:
        Optional[TreeNode]: The node containing the target value, or None if the target is not found.

        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)

        >>> dfs_inorder_search_recursive(root, 5)
        <TreeNode object at ...>  # The node containing the value 5

        >>> dfs_inorder_search_recursive(root, 7)
        None
        """
        if root is None:
            return None

        # Search in the left subtree
        left_result = self.dfs_inorder_search_recursive(root.left, target)
        if left_result is not None:
            return left_result

        # Check the current node
        if root.val == target:
            return root

        # Search in the right subtree
        return self.dfs_inorder_search_recursive(root.right, target)

    def dfs_inorder_search_iterative(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Performs an iterative in-order search in a binary tree to find a node with a specific value.

        In in-order traversal, nodes are visited in the following order:
        1. Left subtree
        2. Current node
        3. Right subtree

        Args:
        root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.
        target (int): The value to search for in the tree.

        Returns:
        Optional[TreeNode]: The node containing the target value, or None if the target is not found.

        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)

        >>> dfs_inorder_search_iterative(root, 5)
        <TreeNode object at ...>  # The node containing the value 5

        >>> dfs_inorder_search_iterative(root, 7)
        None
        """
        stack = deque()
        current = root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()

            if current.val == target:
                return current

            current = current.right

        return None

    def dfs_preorder_search_recursive(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Performs a recursive pre-order search in a binary tree to find a node with a specific value.

        In pre-order traversal, nodes are visited in the following order:
        1. Current node
        2. Left subtree
        3. Right subtree

        Args:
        root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.
        target (int): The value to search for in the tree.

        Returns:
        Optional[TreeNode]: The node containing the target value, or None if the target is not found.

        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)

        >>> dfs_preorder_search_recursive(root, 5)
        <TreeNode object at ...>  # The node containing the value 5

        >>> dfs_preorder_search_recursive(root, 7)
        None
        """
        if root is None:
            return None

        # Check the current node
        if root.val == target:
            return root

        # Search in the left subtree
        left_result = self.dfs_preorder_search_recursive(root.left, target)
        if left_result is not None:
            return left_result

        # Search in the right subtree
        return self.dfs_preorder_search_recursive(root.right, target)

    def dfs_preorder_search_iterative(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Performs an iterative pre-order search in a binary tree to find a node with a specific value.

        In pre-order traversal, nodes are visited in the following order:
        1. Current node
        2. Left subtree
        3. Right subtree

        Args:
        root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.
        target (int): The value to search for in the tree.

        Returns:
        Optional[TreeNode]: The node containing the target value, or None if the target is not found.

        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)

        >>> dfs_preorder_search_iterative(root, 5)
        <TreeNode object at ...>  # The node containing the value 5

        >>> dfs_preorder_search_iterative(root, 7)
        None
        """
        if root is None:
            return None

        stack = deque([root])

        while stack:
            node = stack.pop()

            # Check the current node
            if node.val == target:
                return node

            # Push right child first so that the left child is processed first
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return None

    def dfs_postorder_search_recursive(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Performs a recursive post-order search in a binary tree to find a node with a specific value.

        In post-order traversal, nodes are visited in the following order:
        1. Left subtree
        2. Right subtree
        3. Current node

        Args:
        root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.
        target (int): The value to search for in the tree.

        Returns:
        Optional[TreeNode]: The node containing the target value, or None if the target is not found.

        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)

        >>> dfs_postorder_search_recursive(root, 5)
        <TreeNode object at ...>  # The node containing the value 5

        >>> dfs_postorder_search_recursive(root, 7)
        None
        """
        if root is None:
            return None

        # Search in the left subtree
        left_result = self.dfs_postorder_search_recursive(root.left, target)
        if left_result is not None:
            return left_result

        # Search in the right subtree
        right_result = self.dfs_postorder_search_recursive(root.right, target)
        if right_result is not None:
            return right_result

        # Check the current node
        if root.val == target:
            return root

        return None

    def dfs_postorder_search_iterative(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        """
        Performs an iterative post-order search in a binary tree to find a node with a specific value.

        In post-order traversal, nodes are visited in the following order:
        1. Left subtree
        2. Right subtree
        3. Current node

        Args:
        root (Optional[TreeNode]): The root node of the binary tree. If the tree is empty, this will be None.
        target (int): The value to search for in the tree.

        Returns:
        Optional[TreeNode]: The node containing the target value, or None if the target is not found.

        Example:
        --------
        # Tree structure:
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(6)

        >>> dfs_postorder_search_iterative(root, 5)
        <TreeNode object at ...>  # The node containing the value 5

        >>> dfs_postorder_search_iterative(root, 7)
        None
        """
        if root is None:
            return None

        stack1 = deque([root])
        stack2 = deque()

        # Perform a modified pre-order traversal to simulate post-order
        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)

        # Now traverse the stack2 which contains nodes in post-order
        while stack2:
            node = stack2.pop()
            if node.val == target:
                return node

        return None
