class Node:
    """
        A node in a singly linked list.

        Attributes:
            val (int): The value stored in the node.
            next (Node): The reference to the next node in the list.
    """
    
    def __init__(self, val: int):
        """
            Initializes a new node with the given value.

            Args:
                val (int): The value to be stored in the node.
        """
        self.val = val
        self.next = None


class LinkedListImpl:
    """
        A simple implementation of a singly linked list.

        Attributes:
            head (Node): The head node of the linked list.
            length (int): The length of the linked list.
    """

    def __init__(self):
        """
            Initializes a new instance of the LinkedListImpl class.
        """
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
            Retrieves the value at the specified index in the linked list.

            Args:
                index (int): The index of the node whose value is to be retrieved.

            Returns:
                int: The value at the specified index, or -1 if the index is out of bounds.
        """
        current = self.head
        for i in range(index):
            if not current:
                return -1  # index is out of bounds
            current = current.next
        if not current:
            return -1  # index is out of bounds
        return current.val

    def addAtHead(self, val: int) -> None:
        """
            Adds a node with the specified value at the head of the linked list.

            Args:
                val (int): The value to be added to the new head node.
        """
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val: int) -> None:
        """
            Adds a node with the specified value at the tail of the linked list.

            Args:
                val (int): The value to be added to the new tail node.
        """
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        current_element = self.head

        while current_element.next:
            current_element = current_element.next

        current_element.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        """
            Adds a node with the specified value at the specified index in the linked list.

            Args:
                index (int): The index at which the new node is to be added.
                val (int): The value to be added to the new node.
        """
        if index < 0:
            raise IndexError("Index cannot be negative")

        new_node = Node(val)

        if index == 0:
            self.addAtHead(val)
            return
        
        current = self.head
        
        for i in range(index - 1):
            if not current:
                return  # index is out of bounds
            current = current.next
        
        if not current:
            return  # index is out of bounds
        
        new_node.next = current.next
        current.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        """
            Deletes the node at the specified index in the linked list.

            Args:
                index (int): The index of the node to be deleted.
        """
        if not self.head:
            raise Exception("Empty Linked List")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for i in range(index - 1):
            if not current.next:
                return  # index is out of bounds
            current = current.next
        if not current.next:
            return  # index is out of bounds
        current.next = current.next.next

    def print_list(self) -> None:
        """
            Prints the values of the nodes in the linked list.
        """
        current = self.head 
        while current:
            print(current.val, end=" ") 
            current = current.next  # Move to the next node
        print() 

    def set_length(self) -> None:
        """
            Sets the length attribute of the linked list by counting the nodes.
        """
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        self.length = length
        print(f"Current list length is {length}")

    def is_empty(self) -> bool:
        """
            Checks if the linked list is empty.

            Returns:
                bool: True if the linked list is empty, False otherwise.
        """
        return self.head is None