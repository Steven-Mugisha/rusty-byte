# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dm_helper(root, dm):
            if root is None:
                return 0, dm
            
            else:
                lh, dm = dm_helper(root.left, dm)
                rh, dm = dm_helper(root.right, dm)

                dm = max(dm, lh+rh)

                return max(lh, rh) + 1, dm
        
        diameter = 0
        _, diameter = dm_helper(root, diameter)
        
        return diameter