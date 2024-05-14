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
        if not root:
            return None
        
        current_node = root
        
        while current_node:
            if current_node.left:
                last = current_node.left

                while last.right:
                    last = last.right
                
                last.right = current_node.right
                current_node.right = current_node.left
                current_node.left = None
            
            current_node = current_node.right
        
        return root
