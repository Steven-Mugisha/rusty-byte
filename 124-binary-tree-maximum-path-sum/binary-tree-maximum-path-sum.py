# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_sum_helper(root):
            if not root:
                return 0
            
            root_leftSum = max_sum_helper(root.left)
            root_rightSum = max_sum_helper(root.right)

            leftTree, rightTree = 0,0

            if root_leftSum > 0:
                leftTree = root_leftSum
            
            if root_rightSum > 0:
                rightTree = root_rightSum
            
            valSum_newPath = root.val + leftTree + rightTree
            
            max_sum = max_sum_helper.max_sum

            max_sum_helper.max_sum = max(max_sum, valSum_newPath)

            return root.val + max(leftTree, rightTree)
        
        max_sum_helper.max_sum = float("-inf")

        max_sum_helper(root)

        return max_sum_helper.max_sum