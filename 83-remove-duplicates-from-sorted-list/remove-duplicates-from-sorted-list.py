# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        dummy = ListNode(0)
        dummy.next = head

        while head.next:
            if head.val == head.next.val:
                del_node = head.next
                head.next = del_node.next
                del_node.next = None
            
            else:
                head = head.next
        
        return dummy.next
        


