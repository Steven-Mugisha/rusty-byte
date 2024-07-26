# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # if not root.left and not root.right = 0
        # ans += root.left; condition: root.left has no children.
        # ans += root.right;

        if not root.left and not root.right:
            return 0
        
        ans = 0

        if root.left:
            if not root.left.left and not root.left.right:
                ans += root.left.val
            
            else:
                ans += self.sumOfLeftLeaves(root.left)
            
        if root.right:
            ans += self.sumOfLeftLeaves(root.right)
        
        return ans
