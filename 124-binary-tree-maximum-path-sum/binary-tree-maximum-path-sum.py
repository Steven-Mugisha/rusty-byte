# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPathSum_rec(root):
            if not root:
                return 0
            
            rootleftTree = maxPathSum_rec(root.left)
            rootrightTree = maxPathSum_rec(root.right)

            left, right = 0, 0

            if rootleftTree > 0: left = rootleftTree
            if rootrightTree > 0: right = rootrightTree

            valPathsum = root.val + left + right

            maxSum = maxPathSum_rec.maxSum
            maxPathSum_rec.maxSum = max(maxSum, valPathsum)

            return root.val + max(left, right)

        maxPathSum_rec.maxSum = float("-inf")
            
        maxPathSum_rec(root)

        return maxPathSum_rec.maxSum




