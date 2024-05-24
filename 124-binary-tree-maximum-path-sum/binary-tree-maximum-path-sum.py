# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxContrib(root):
            if not root:
                return 0
            
            maxLeftSum = maxContrib(root.left)
            maxRightSum = maxContrib(root.right)

            leftTree, rightTree = 0, 0

            if maxLeftSum > 0: leftTree = maxLeftSum
            if maxRightSum > 0: rightTree = maxRightSum

            newPathSum = root.val + leftTree + rightTree

            maxSum = maxContrib.maxSum
            maxContrib.maxSum = max(maxSum, newPathSum)

            return root.val + max(leftTree, rightTree)
        
        maxContrib.maxSum = float("-inf")
        maxContrib(root)

        return maxContrib.maxSum