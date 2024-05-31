# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return
        
        currentNode = root

        while currentNode:
            if currentNode.left:
                last = currentNode.left
                while last.right:
                    last = last.right
                last.right = currentNode.right
                currentNode.right = currentNode.left
                currentNode.left = None
            
            currentNode = currentNode.right
        
        return currentNode
                

