"""
    A module that implements a singly linked list and its basic operations.

    Classes:
        Node: Represents a node in a singly linked list.
        LinkedListImpl: Represents a singly linked list with methods for various operations.

    Example usage:
        # Create a new linked list
        linked_list = LinkedListImpl()

        # Add elements to the linked list
        linked_list.addAtHead(1)
        linked_list.addAtTail(3)
        linked_list.addAtIndex(1, 2)  # Linked list becomes 1 -> 2 -> 3

        # Get an element from the linked list
        value = linked_list.get(1)  # Returns 2

        # Delete an element from the linked list
        linked_list.deleteAtIndex(1)  # Linked list becomes 1 -> 3

        # Print the linked list
        linked_list.print_list()  # Outputs: 1 3

        # Check if the linked list is empty
        is_empty = linked_list.is_empty()  # Returns False

        # Set and get the length of the linked list
        linked_list.set_length()  # Outputs: Current list length is 2
        length = linked_list.length  # Returns 2
"""

class HashMapImpl:
    """
        A simple implementation of a hash map using a list for internal storage.

        Attributes:
            hashmap (list): A list to store the key-value pairs of the hash map.
    """

    def __init__(self, size: int):
        """
            Initializes a new instance of the HashMapImpl class.

            Args:
                size (int): The initial size of the hash map.
        """
        self.hashmap = [[] for _ in range(size)]

    def put(self, key: int, value: int) -> None:
        """
            Inserts a key-value pair into the hash map.

            Args:
                key (int): The key to be inserted.
                value (int): The value to be associated with the key.
        """
        self.hashmap[key] = value

    def get(self, key: int) -> int:
        """
            Retrieves the value associated with the specified key.

            Args:
                key (int): The key whose associated value is to be returned.

            Returns:
                int: The value associated with the specified key, or -1 if the key is not found.
        """
        return -1 if key >= len(self.hashmap) or self.hashmap[key] == [] else self.hashmap[key]

    def remove(self, key: int) -> None:
        """
            Removes the key-value pair associated with the specified key.

            Args:
                key (int): The key whose key-value pair is to be removed.
        """
        if key < len(self.hashmap) and self.hashmap[key] != []:
            self.hashmap[key] = []
