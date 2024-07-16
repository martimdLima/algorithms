# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        pal = []
        while current:
            pal.append(current.val)
            current = current.next
        return pal == list(reversed(pal))
    
    def isPalindrome(head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # Step 1: Find the middle of the linked list
        mid, end = head, head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        
        # Step 3: Compare the first and second half
        left, right = head, prev
        while right:  # Only need to compare till end of right half
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True