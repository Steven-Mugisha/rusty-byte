# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        return self.sortedArrayHelper(nums, 0, len(nums) - 1)
    
    def sortedArrayHelper(self, nums, low, high):
        if low > high: return None

        mid_val = (high + low) //2

        node = TreeNode(nums[mid_val])
        node.left = self.sortedArrayHelper(nums, low, mid_val - 1)
        node.right = self.sortedArrayHelper(nums, mid_val + 1, high)

        return node