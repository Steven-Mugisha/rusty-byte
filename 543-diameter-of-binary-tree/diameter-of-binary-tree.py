# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, dm):
            if not node:
                return 0, dm
            
            else:
                lh, dm = dfs(node.left, dm)
                rh, dm = dfs(node.right, dm)

                dm = max(dm, lh + rh)

                return max(lh, rh) + 1, dm
        
        diameter = 0
        _, diameter = dfs(root, diameter)

        return diameter

    