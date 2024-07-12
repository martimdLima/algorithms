class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        current = self.head
        for i in range(index):
            if not current:
                return -1  # index is out of bounds
            current = current.next
        if not current:
            return -1  # index is out of bounds
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            print(f"List has no current head, adding new node {new_node.val} as head")
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

        print(f"Added new node after the head, with val {new_node.val}")

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)

        if not self.head:
            self.head = new_node
            return

        current_element = self.head

        while current_element.next:
            current_element = current_element.next

        current_element.next = new_node

        print(f"Added node with val {new_node.val} at tail")

    def addAtIndex(self, index: int, val: int) -> None:
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

    def print_list(self):
        current = self.head  # Start from the head of the list
        while current:
            print(current.val, end=" ")  # Print the data in the current node
            current = current.next  # Move to the next node
        print()  # Ensures the output is followed by a new line

    def set_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        self.length = length
        print(f"Current list length is {length}")

    def is_empty(self):
        return self.head is None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
