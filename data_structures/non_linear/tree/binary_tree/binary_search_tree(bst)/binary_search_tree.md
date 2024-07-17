# Binary Search Tree (BST)

## Definition
A Binary Search Tree (BST) is a binary tree data structure where each node has at most two children, referred to as the left child and the right child. The key property of a BST is that the key (or value) of a node's left child is less than its parent's key, and the key of the node's right child is greater than or equal to its parent's key. This ordering makes it efficient for searching, inserting, and deleting nodes in the tree.

## Properties of a Binary Search Tree:
1. **Ordering Property**: For every node  $𝑁$ n the BST, the values in  $𝑁$'s left subtree are less than  $𝑁$'s value, and the values in  $𝑁$'s right subtree are greater than or equal to  $𝑁$'s value.
2. **Unique Nodes**: No duplicate nodes are allowed in a BST (however, some variants may allow duplicates).
3. **Recursive Structure**: Each subtree of a BST is itself a BST.

## Aplications
1. **Searching**: BSTs are efficient for searching operations due to their ordered structure. The time complexity for searching, inserting, and deleting operations is $𝑂(ℎ)$, where  $ℎ$ is the height of the tree (balanced BSTs have $ℎ=log𝑛$ in the average case).
2. **Ordered Iteration**: In-order traversal of a BST yields keys in sorted order, making it suitable for applications requiring sorted data.
3. **Symbol Tables**: BSTs are used as the basis for implementing symbol tables in compilers, where quick lookup, insert, and delete operations are crucial.
4. **Range Queries**: BSTs can efficiently support range queries, such as finding all elements within a given range of values.

## Advantages:
1. **Efficient Search**: Average time complexity for search, insert, and delete operations is $𝑂(log𝑛)$, making BSTs suitable for large datasets.
2. **Ordered Structure**: Maintains data in sorted order, facilitating in-order traversal for sorted data retrieval.
3. **Versatility**: BSTs can be augmented for additional functionalities such as balancing (AVL trees, Red-Black trees) or handling specific requirements (e.g., handling duplicates).

## Disadvantages:
1. **Unbalanced Trees**: In worst-case scenarios (e.g., inserting sorted data), BSTs can become unbalanced, leading to performance degradation $𝑂(𝑛)$ for search and other operations.
2. **Complex Operations**: Insertion and deletion operations may require tree restructuring (rotation), which adds complexity compared to simpler data structures like arrays or linked lists.

## Minimal Implementation of a Binary Search Tree
``` python
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_recursive(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_recursive(root.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search_recursive(root.left, key)
        else:
            return self._search_recursive(root.right, key)


# Example usage:
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print(bst.search(60))
print(bst.search(90))
```