# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        while current:
            temp = current.next
            current.next = previous
            previous, current = current, temp

        return previous

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(previous, current):
            if not current:
                return previous

            temp = current.next
            current.next = previous
            previous, current = current, temp

            return reverse(previous, current)

        return reverse(None, head)
