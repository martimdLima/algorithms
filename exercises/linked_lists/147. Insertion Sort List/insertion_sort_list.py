def insertion_sort_list(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    # Create a new node to act as the new sorted list's head
    sorted_list = ListNode(float("-inf"))

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
