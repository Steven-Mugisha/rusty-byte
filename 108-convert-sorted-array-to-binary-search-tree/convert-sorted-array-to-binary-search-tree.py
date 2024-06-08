# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper_to_bst(nums, first, last):
            if first > last:
                return
            
            mid = (first + last) // 2
            root = TreeNode(nums[mid])

            root.left = helper_to_bst(nums, first, mid - 1)
            root.right = helper_to_bst(nums, mid + 1, last)

            return root
        
        return helper_to_bst(nums, 0, len(nums) - 1)
    