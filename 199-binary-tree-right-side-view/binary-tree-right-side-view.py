# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, arr, level):
            if level == len(arr):
                arr.append(root.val)
            
            for root_child in [root.right, root.left]:
                if root_child != None:
                    dfs(root_child, arr, level + 1)
        
        if not root: return None
        arr = []
        dfs(root, arr, 0)

        return arr
