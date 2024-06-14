# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root, rSide, level):
            if not root: return
            if level == len(rSide):
                rSide.append(root.val)
            dfs(root.right, rSide, level + 1)
            dfs(root.left, rSide, level + 1)
        
        if not root: return []
        rSide = []
        dfs(root, rSide, 0)
        
        return rSide
            