from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BreadthFirstForGraphs:
    """
    Provides methods to perform Breadth-First Search (BFS) on a graph.

    This class includes both iterative and recursive implementations for
    traversing and searching through graph structures represented as adjacency lists.
    """

    def bfs_graph_transversal_iterative(self, graph: dict, start: int) -> list:
        """
        Performs an iterative Breadth-First Search (BFS) traversal on a graph.

        Args:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      The keys are node identifiers, and the values are lists of adjacent nodes.
        start (int): The starting node for the BFS traversal.

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
        >>> bfs_graph_transversal_iterative(graph, 0)
        [0, 1, 2, 3, 4, 5]
        """
        visited = set()
        queue = deque([start])
        visited.add(start)
        bfs_order = []

        while queue:
            node = queue.popleft()
            bfs_order.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return bfs_order

    def bfs_graph_transversal_recursive(self, graph: dict, start: int) -> list:
        """
        Performs a recursive Breadth-First Search (BFS) traversal on a graph.

        Args:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      The keys are node identifiers, and the values are lists of adjacent nodes.
        start (int): The starting node for the BFS traversal.

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
        >>> bfs_graph_transversal_recursive(graph, 0)
        [0, 1, 2, 3, 4, 5]
        """

        def bfs_recursive(queue, visited):
            if not queue:
                return []

            node = queue.popleft()
            visited.add(node)
            bfs_order = [node]

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

            return bfs_order + bfs_recursive(queue, visited)

        visited = set()
        queue = deque([start])
        visited.add(start)
        return bfs_recursive(queue, visited)

    def bfs_graph_search_iterative(self, graph: dict, start: int, target: int) -> int:
        """
        Performs an iterative Breadth-First Search (BFS) to find a target element in a graph.

        Args:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      The keys are node identifiers, and the values are lists of adjacent nodes.
        start (int): The starting node for the BFS traversal.
        target (int): The element to search for in the graph.

        Returns:
        int: The node identifier where the target is found, or None if the target is not present.

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
        >>> bfs_graph_search_iterative(graph, 0, 5)
        5

        >>> bfs_graph_search_iterative(graph, 0, 6)
        None
        """
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()

            if node == target:
                return node

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return None

    def bfs_graph_search_recursive(self, graph: dict, start: int, target: int) -> int:
        """
        Performs a recursive Breadth-First Search (BFS) to find a target element in a graph.

        Args:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      The keys are node identifiers, and the values are lists of adjacent nodes.
        start (int): The starting node for the BFS traversal.
        target (int): The element to search for in the graph.

        Returns:
        int: The node identifier where the target is found, or None if the target is not present.

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
        >>> bfs_graph_search_recursive(graph, 0, 5)
        5

        >>> bfs_graph_search_recursive(graph, 0, 6)
        None
        """

        def bfs_recursive(queue, visited):
            if not queue:
                return None

            node = queue.popleft()
            if node == target:
                return node

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

            return bfs_recursive(queue, visited)

        visited = set()
        queue = deque([start])
        visited.add(start)
        return bfs_recursive(queue, visited)
        """
        Performs a Breadth-First Search (BFS) to find a target element in a graph.

        Args:
        graph (dict): A dictionary representing the adjacency list of the graph.
                      The keys are node identifiers, and the values are lists of adjacent nodes.
        start (int): The starting node for the BFS traversal.
        target (int): The element to search for in the graph.

        Returns:
        int: The node identifier where the target is found, or None if the target is not present.

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
        >>> bfs_search_graph(graph, 0, 5)
        5

        >>> bfs_search_graph(graph, 0, 6)
        None
        """
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()

            if node == target:
                return node

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return None


class BreadthFirstForTrees:
    """
    Provides methods to perform Breadth-First Search (BFS) on a binary tree.

    This class includes both iterative and recursive implementations for
    traversing and searching through binary tree structures.
    """

    def bfs_tree_transversal_iterative(self, root: TreeNode) -> list:
        """
        Performs an iterative Breadth-First Search (BFS) traversal on a binary tree.

        Args:
        root (TreeNode): The root node of the binary tree.

        Returns:
        list: A list of values of the nodes in the order they were visited.

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
        
        >>> bfs_tree_transversal_iterative(root)
        [1, 2, 3, 4, 5, 6]
        """
        if not root:
            return []
        queue = deque([root])
        bfs_order = []
        while queue:
            node = queue.popleft()
            bfs_order.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return bfs_order

    def bfs_tree_transversal_recursive(self, root: TreeNode) -> list:
        """
        Performs a recursive Breadth-First Search (BFS) traversal on a binary tree.

        Args:
        root (TreeNode): The root node of the binary tree.

        Returns:
        list: A list of values of the nodes in the order they were visited.

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
        
        >>> bfs_tree_transversal_recursive(root)
        [1, 2, 3, 4, 5, 6]
        """

        def bfs_recursive(queue):
            if not queue:
                return []

            node = queue.popleft()
            bfs_order = [node.val]

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            return bfs_order + bfs_recursive(queue)

        if not root:
            return []
        queue = deque([root])
        return bfs_recursive(queue)

    def bfs_search_tree_iterative(self, root: TreeNode, target: int) -> TreeNode:
        """
        Performs an iterative Breadth-First Search (BFS) to find a target value in a binary tree.

        Args:
        root (TreeNode): The root node of the binary tree.
        target (int): The value to search for in the tree.

        Returns:
        TreeNode: The node containing the target value, or None if the target is not found.

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
        
        >>> bfs_search_tree_iterative(root, 5)
        <TreeNode object at ...>  # The node containing the value 5

        >>> bfs_search_tree_iterative(root, 7)
        None
        """
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == target:
                return node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return None

    def bfs_search_tree_recursive(self, root: TreeNode, target: int) -> TreeNode:
        """
        Performs a recursive Breadth-First Search (BFS) to find a target value in a binary tree.

        Args:
        root (TreeNode): The root node of the binary tree.
        target (int): The value to search for in the tree.

        Returns:
        TreeNode: The node containing the target value, or None if the target is not found.

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
        
        >>> bfs_search_tree_recursive(root, 5)
        <TreeNode object at ...>  # The node containing the value 5

        >>> bfs_search_tree_recursive(root, 7)
        None
        """

        def bfs_recursive(queue):
            if not queue:
                return None

            node = queue.popleft()
            if node.val == target:
                return node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            return bfs_recursive(queue)

        if not root:
            return None
        queue = deque([root])
        return bfs_recursive(queue)
