"""
    A module that implements a simple hash set using a dictionary for internal storage.

    Classes:
        HashSetImpl: Represents a hash set with methods for adding, removing, and checking elements.

    Example usage:
        # Create a new hash set
        hash_set = HashSetImpl()

        # Add elements to the hash set
        hash_set.add(1)
        hash_set.add(2)

        # Check if elements are in the hash set
        print(hash_set.contains(1))  # Outputs: True
        print(hash_set.contains(3))  # Outputs: False

        # Remove an element from the hash set
        hash_set.remove(1)

        # Check if the element is still in the hash set
        print(hash_set.contains(1))  # Outputs: False
"""

class HashSetImpl:
    """
        A simple implementation of a hash set using a dictionary for internal storage.

        Attributes:
            hash_set (dict): A dictionary to store the elements of the hash set.
    """

    def __init__(self):
        """
            Initializes a new instance of the HashSetImpl class.
        """
        self.hash_set = {}

    def add(self, key: int) -> None:
        """
            Adds an element to the hash set.

            Args:
                key (int): The element to be added to the hash set.
        """
        if not self.contains(key):
            self.hash_set[key] = key

    def remove(self, key: int) -> None:
        """
            Removes an element from the hash set if it exists.

            Args:
                key (int): The element to be removed from the hash set.
        """
        if self.contains(key):
            del self.hash_set[key]

    def contains(self, key: int) -> bool:
        """
            Checks if an element is present in the hash set.

            Args:
                key (int): The element to check for presence in the hash set.

            Returns:
                bool: True if the element is present, False otherwise.
        """
        return key in self.hash_set
