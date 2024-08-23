# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        left, right = head, head

        while n > 0:
            right = right.next
            n -= 1
        
        if not right:
            return head.next
        
        while right.next:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return head



        
