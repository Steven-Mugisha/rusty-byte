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
            
            leftTreeSum = maxPathSum_rec(root.left)
            rightTreeSum = maxPathSum_rec(root.right)

            left, right = 0, 0

            if leftTreeSum > 0: left = leftTreeSum
            if rightTreeSum > 0: right = rightTreeSum

            currentPathSum = root.val + left + right

            maxSum = maxPathSum_rec.maxSum
            maxPathSum_rec.maxSum = max(maxSum, currentPathSum)

            return root.val + max(left, right)

        maxPathSum_rec.maxSum = float("-inf")
            
        maxPathSum_rec(root)

        return maxPathSum_rec.maxSum




