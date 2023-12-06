# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        if head:
            curr = head
            last_check = head
        
        length = 0
        index_node = 0
        res_node = 0
        
        while curr:
            length += 1
            curr = curr.next
        
        index_node = (length // 2) + 1

        while index_node and last_check:
            res_node = last_check
            last_check = last_check.next
            index_node -= 1
        
        return res_node





    

    
