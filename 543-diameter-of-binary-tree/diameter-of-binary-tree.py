# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        if not root:
            return 0

        _, diameter = self.diameterHelper(root, diameter)
        return diameter
    

    def diameterHelper(self, node, diameter):
        if not node:
            return 0, diameter
        else:
            lh, diameter = self.diameterHelper(node.left, diameter)
            rh, diameter = self.diameterHelper(node.right, diameter)

            diameter = max(diameter, lh+rh)
            return max(lh,rh) + 1, diameter

    
        