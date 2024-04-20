# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = None
        current_node = head

        while current_node:
            after = current_node.next
            current_node.next = before
            before = current_node
            current_node = after

        return before


            
        