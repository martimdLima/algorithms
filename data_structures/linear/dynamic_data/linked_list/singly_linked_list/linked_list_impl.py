from typing import Any, Optional


class Node:
    """
    Represents a single node in a linked list.

    Attributes:
        data (Any): The data stored in the node.
        next (Optional[Node]): The next node in the linked list.
    """

    def __init__(self, data=None):
        """
        Initializes a new node with the given data and sets the next pointer to None.

        Args:
            data (Any, optional): The data to store in the node. Defaults to None.
        """
        self.data = data
        self.next = None


class LinkedListImpl:
    """
    Represents a singly linked list.

    Attributes:
        head (Optional[Node]): The head node of the linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list with the head set to None.
        """
        self.head = None

    def append(self, data: Any) -> None:
        """
        Appends a new node with the given data to the end of the list.

        Args:
            data (Any): The data to store in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data: Any) -> None:
        """
        Inserts a new node with the given data at the beginning of the list.

        Args:
            data (Any): The data to store in the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, key: Any) -> bool:
        """
        Searches for a node with the given data in the list.

        Args:
            key (Any): The data to search for.

        Returns:
            bool: True if a node with the given data is found, False otherwise.
        """
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def search_at_index(self, index: int) -> Optional[Any]:
        """
        Searches for a node at the given index in the list.

        Args:
            index (int): The index to search for.

        Returns:
            Optional[Any]: The data at the given index if found, None otherwise.
        """
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None  # Index is out of bounds

    def get_middle_element(self, head: Optional[Node]) -> Optional[Node]:
        """
        Finds the middle element of the linked list.

        Args:
            head (Optional[Node]): The head node of the linked list.

        Returns:
            Optional[Node]: The middle node of the linked list.
        """
        if head is None:
            return head

        left = head
        right = head

        while right.next is not None and right.next.next is not None:
            left = left.next
            right = right.next.next

    def delete(self, key: Any) -> None:
        """
        Deletes the first node with the given data from the list.

        Args:
            key (Any): The data to delete from the list.
        """
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def delete_at_index(self, index: int) -> None:
        """
        Deletes the node at the given index from the list.

        Args:
            index (int): The index of the node to delete.
        """
        if self.head is None:
            return

        temp = self.head

        if index == 0:
            self.head = temp.next
            temp = None
            return

        count = 0
        prev = None
        while temp is not None:
            if count == index:
                break
            prev = temp
            temp = temp.next
            count += 1

        if temp is None:
            return  # Index is out of bounds

        prev.next = temp.next
        temp = None

    def merge_sorted_lists(
        self, left_side: Optional[Node], right_side: Optional[Node]
    ) -> Optional[Node]:
        """
        Merges two sorted linked lists into one sorted list.

        Args:
            left_side (Optional[Node]): The head node of the first sorted list.
            right_side (Optional[Node]): The head node of the second sorted list.

        Returns:
            Optional[Node]: The head node of the merged sorted list.
        """
        result = None

        if left_side is None:
            return right_side

        if right_side is None:
            return left_side

        if left_side.val <= right_side.val:
            result = left_side
            result.next = self.merge_sorted_lists(left_side.next, right_side)
        else:
            result = right_side
            result.next = self.merge_sorted_lists(left_side, right_side.next)
        return result

    def insertion_sort(self, head: Optional[Node]) -> Optional[Node]:
        """
        Sorts the linked list using the insertion sort algorithm.

        Args:
            head (Optional[Node]): The head node of the linked list to sort.

        Returns:
            Optional[Node]: The head node of the sorted linked list.
        """
        if not head or not head.next:
            return head

        # Create a new node to act as the new sorted list's head
        sorted_list = Node(float("-inf"))

        while head:
            # At each step, remove the node from the original list
            current = head
            head = head.next

            # Find the position to insert the current node in the sorted list
            previous = sorted_list
            while previous.next and previous.next.value < current.value:
                previous = previous.next

            # Insert the current node into the sorted list
            current.next = previous.next
            previous.next = current

        # return the actual head of the sorted list
        return sorted_list.next

    def merge_sort(self, head: Optional[Node]) -> Optional[Node]:
        """
        Sorts the linked list using the merge sort algorithm.

        Args:
            head (Optional[Node]): The head node of the linked list to sort.

        Returns:
            Optional[Node]: The head node of the sorted linked list.
        """
        if head is None or head.next is None:
            return head

        middle = self.get_middle_element(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sortedlist = self.merge_sorted_lists(left, right)

        return sortedlist

    def is_empty(self) -> bool:
        """
        Checks if the linked list is empty.

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self.head is None

    def print_list(self) -> None:
        """
        Prints the linked list.
        """
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")
