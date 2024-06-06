# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def helperSortedArray(nums, low, high):
            if low > high: 
                return None
            
            else:
                mid = (high + low) // 2
                root = TreeNode(nums[mid])
                root.left = helperSortedArray(nums, low, mid - 1)
                root.right = helperSortedArray(nums, mid + 1, high)
            
            return root
        
        return helperSortedArray(nums, 0, len(nums)-1)