# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative approach
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None

        while head:
            new_node = ListNode(head.val)
            new_node.next = new_head
            new_head = new_node
            head = head.next

        return new_head

    # Recursive approach 1
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(head: Optional[ListNode], new_head: Optional[ListNode]):
            if not head:
                return new_head

            new_node = ListNode(head.val)
            new_node.next = new_head
            new_head = new_node
            head = head.next

            return reverse_list(head, new_head)

        new_head = None

        return reverse_list(head, new_head)

    # Recursive approach 2
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(
            current: Optional[ListNode], previous: Optional[ListNode] = None
        ) -> Optional[ListNode]:
            if not current:
                return previous
            next_node = current.next
            current.next = previous
            return reverse_list(next_node, current)

        return reverse_list(head)
