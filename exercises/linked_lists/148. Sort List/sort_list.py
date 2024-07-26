# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_middle_element(self, head):
        if head is None:
            return head

        left = head
        right = head

        while right.next is not None and right.next.next is not None:
            left = left.next
            right = right.next.next

        return left

    def merge_sorted_lists(self, left_side, right_side):
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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        middle = self.get_middle_element(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.sortList(head)
        right = self.sortList(next_to_middle)

        sortedlist = self.merge_sorted_lists(left, right)

        return sortedlist
