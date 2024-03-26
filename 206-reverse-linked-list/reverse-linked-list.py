# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        node = head
        while node:
            after = node.next
            node.next = ans
            ans = node
            node = after
        
        return ans

            
        