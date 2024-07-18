# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0)
        previous = head

        while list1 is not None or list2 is not None:
            if list1 is None:
                previous.next = list2
                break

            if list2 is None:
                previous.next = list1
                break

            if list1.val <= list2.val:
                previous.next = list1
                list1 = list1.next
            else:
                previous.next = list2
                list2 = list2.next

            previous = previous.next

        return head.next
