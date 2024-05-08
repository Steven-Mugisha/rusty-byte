# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1String = ""
        l2String = ""

        ans = ListNode()

        l1Pointer, l2Pointer = l1, l2

        while l1Pointer != None:
            l1String += str(l1Pointer.val)
            l1Pointer = l1Pointer.next
        
        while l2Pointer != None:
            l2String += str(l2Pointer.val)
            l2Pointer = l2Pointer.next
        
        sumList = int(l1String[::-1]) + int(l2String[::-1])
        sumList = str(sumList)

        # 807
        curr_index = 0
        while curr_index < len(sumList):
            value = sumList[curr_index]
            node = ListNode(value)
            if curr_index == 0:
                ans.val = value

            else:
                node.next = ans
                ans = node
            
            curr_index += 1
        
        return ans
                
        
      