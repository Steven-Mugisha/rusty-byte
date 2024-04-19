# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # if not head:
        #     return True

        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next  # None
            slow = slow.next
        
        # reverse:
        prev = None
        while slow is not None:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr
        
        first = head
        last = prev

        while last:
            if last.val != first.val:
                return False
            last = last.next
            first = first.next

        # while prev:
        #     if prev.val != head.val:
        #         return False

        #     prev = prev.next
        #     head = head.next
        
        return True




        





        







