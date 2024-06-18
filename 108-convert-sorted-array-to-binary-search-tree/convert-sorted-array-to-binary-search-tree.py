# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(nums, low, high):
            if low > high: return

            mid = (low + high) // 2

            root = TreeNode(nums[mid])
            root.left = dfs(nums, low, mid - 1)
            root.right = dfs(nums, mid+1, high)

            return root
        
        # if not root return None

        return dfs(nums, 0, len(nums) - 1)