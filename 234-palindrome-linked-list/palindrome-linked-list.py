# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # reach the middle with slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half
        before = None
        while slow:
            after = slow.next
            slow.next = before
            before = slow
            slow = after
        
        # check for palindrome
        while before:
            if before.val != head.val:
                return False
            before = before.next
            head = head.next
        
        return True
        

