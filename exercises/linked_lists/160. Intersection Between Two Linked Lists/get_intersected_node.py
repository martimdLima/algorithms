# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        def get_length(head: Optional[ListNode], size):
            if head == None:
                return size
            return get_length(head.next, size + 1)

        size_a = get_length(headA, 0)
        size_b = get_length(headB, 0)

        is_a_bigger_than_b = size_a >= size_b

        list_a = headA if is_a_bigger_than_b else headB
        list_b = headB if is_a_bigger_than_b else headA
        length_difference = size_a - size_b if is_a_bigger_than_b else size_b - size_a

        while length_difference > 0:
            list_a = list_a.next
            length_difference -= 1

        while list_a != None:
            if list_a == list_b:
                return list_a

            list_a = list_a.next
            list_b = list_b.next
        return None
