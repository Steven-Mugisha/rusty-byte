# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = head
        while temp:
            if temp.next == slow:
                temp.next = temp.next.next
                slow.next = None
                return head
            else:
                temp = temp.next
        
        return 
   
                

