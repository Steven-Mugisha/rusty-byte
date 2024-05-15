# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        sz = 0
        current = head

        while current:
            sz+= 1
            current = current.next

        pos = (sz - n) + 1

        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        
        while temp:
            if (pos -1) == 0:
                temp.next = temp.next.next
                return dummy.next
            pos -= 1
            temp = temp.next



