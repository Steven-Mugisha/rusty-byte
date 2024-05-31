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
        if root is None: return None

        curr_node = root

        while curr_node:
            if curr_node.left:
                last = curr_node.left
                while last.right:
                    last = last.right
                
                last.right = curr_node.right
                curr_node.right = curr_node.left
                curr_node.left = None
            curr_node = curr_node.right
        
        return root